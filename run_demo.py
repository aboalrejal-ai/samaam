#!/usr/bin/env python3
"""مشغّل السيناريوهات الثلاثة من الطرفية.

    python run_demo.py            # الثلاثة
    python run_demo.py 2          # سيناريو بعينه
    python run_demo.py 2 --override "Dr. A. Alharbi, Consultant Radiologist"
"""
from __future__ import annotations

import argparse
import json
import sys

from app.config import settings
from app.pipeline import Samaam

C = {"g": "\033[92m", "r": "\033[91m", "y": "\033[93m", "b": "\033[94m",
     "d": "\033[2m", "B": "\033[1m", "0": "\033[0m"}
ICON = {"PASS": "✅", "FAIL": "❌", "WARN": "⚠️ ", "NOT_APPLICABLE": "  ",
        "NO_EVIDENCE": "❓"}


def rule(ch: str = "─") -> None:
    print(C["d"] + ch * 78 + C["0"])


def run_one(s: Samaam, sc: dict, override: str | None) -> bool:
    print()
    rule("━")
    print(f"{C['B']}{sc['id']} · {sc['name']}{C['0']}  {C['d']}{sc['name_en']}{C['0']}")
    rule("━")

    if sc["id"] == "SC-03":
        req = sc["request"]
        print(f"{C['d']}الفاعل:{C['0']} {req['actor']}")
        print(f"{C['d']}الطلب:{C['0']}  {req['action'][:68]}…")
        print(f"{C['d']}الغرض:{C['0']}  {req['stated_purpose']}\n")

        result = s.run_data_request({
            "request_id": "DATA-REQ-SC03", "actor": req["actor"],
            "action": req["action"], "stated_purpose": req["stated_purpose"],
            "record_count": 4200, "destination_outside_kingdom": True,
            "care_purpose": False,
        }, override_by=override)
        pol, dev = result["policy"], result["device_response"]

        for c in pol["checks"]:
            basis = f"{C['d']}[{c['basis']}]{C['0']}" if c["basis"] else ""
            act = f"{C['d']}→ {c.get('action','')}{C['0']}"
            print(f"  {ICON[c['status']]} {c['rule']:<24} {basis} {act}")
            if c["status"] == "FAIL":
                print(f"     {C['d']}{c['detail'][:148]}{C['0']}")

        print(f"\n  {C['B']}الحكم:{C['0']} {C['r']}{pol['verdict']}{C['0']}"
              f"    {C['B']}الاستجابة:{C['0']} {C['r']}HTTP {dev['status']}{C['0']}"
              f"  {C['d']}{dev['message']}{C['0']}")
        print(f"  {C['r']}⛔ قابل للتجاوز: لا{C['0']}  {C['d']}{pol['override_reason'][:88]}{C['0']}")

        if pol.get("explanation"):
            print(f"\n  {C['b']}الشرح:{C['0']}")
            for line in _wrap(pol["explanation"], 72):
                print(f"    {line}")
        print(f"\n  {C['b']}المراجع:{C['0']}")
        for c in pol["citations"]:
            if "error" not in c:
                print(f"    • {C['B']}{c['record_id']}{C['0']} — {c['authority']}, {c['section']}")

        ok = pol["verdict"] == sc["expected_verdict"]
        print(f"\n  {C['g']}✓ مطابق للمتوقع{C['0']}" if ok
              else f"\n  {C['r']}✗ توقعنا {sc['expected_verdict']}{C['0']}")
        return ok

    result = s.run(
        {"worklist_id": f"MWL-{sc['id']}", "patient": sc["patient"],
         "requested": sc["requested"]},
        override_by=override,
    )
    pol, dev = result["policy"], result["device_response"]

    p = sc["patient"]
    print(f"{C['d']}المريض:{C['0']} {p['sex']} · {p['age']} سنة · {p.get('weight_kg')} كغ"
          f" · {p['diagnosis'][:44]}")
    print(f"{C['d']}الكلى:{C['0']}  كرياتينين {p['serum_creatinine_umol_l']} → "
          f"{C['B']}eGFR {p['egfr']}{C['0']}  {C['d']}(CKD-EPI، وزارة الصحة ص21){C['0']}")
    r = sc["requested"]
    print(f"{C['d']}الطلب:{C['0']}  {r['kvp']} kVp · {r['mas']} mAs · "
          f"CTDIvol {r['ctdivol_mgy']} · DLP {r['dlp_mgy_cm']} · صبغة {r['volume_ml']} مل")
    print()

    for c in pol["checks"]:
        basis = f"{C['d']}[{c['basis']}]{C['0']}" if c["basis"] else ""
        act = f"{C['d']}→ {c.get('action','')}{C['0']}"
        print(f"  {ICON[c['status']]} {c['rule']:<20} {basis} {act}")
        if c["status"] in ("FAIL", "WARN", "NO_EVIDENCE"):
            print(f"     {C['d']}{c['detail'][:150]}{C['0']}")
    print()

    ACTION = {"PROCEED": ("🟢", C["g"]), "CONFIRM": ("🟡", C["y"]),
              "AUTHORISE": ("🔴", C["r"]), "PROHIBITED": ("⛔", C["r"])}
    icon, colour = ACTION.get(pol.get("action", ""), ("", C["d"]))
    print(f"  {C['B']}الحكم:{C['0']} {colour}{pol['verdict']}{C['0']}"
          f"    {C['B']}الفعل:{C['0']} {colour}{icon} {pol.get('action','')}{C['0']}"
          f"    {C['B']}الجهاز:{C['0']} {colour}HTTP {dev['status']}{C['0']}")
    print(f"  {C['d']}{dev.get('message', dev.get('error',''))[:74]}{C['0']}")
    print(f"  {C['d']}الخصوصية: حُذفت {result['privacy']['identifiers_removed'] or 'لا معرّفات'}{C['0']}")

    if pol.get("explanation"):
        print(f"\n  {C['b']}الشرح:{C['0']}")
        for line in _wrap(pol["explanation"], 72):
            print(f"    {line}")

    if pol["citations"]:
        print(f"\n  {C['b']}المراجع:{C['0']}")
        for c in pol["citations"]:
            if "error" in c:
                print(f"    {C['r']}⛔ {c['record_id']}: {c['error']}{C['0']}")
                continue
            print(f"    • {C['B']}{c['record_id']}{C['0']} — {c['authority']}, {c['section']}")
            print(f"      {C['d']}{c['url']}{C['0']}")

    ok = pol["verdict"] == sc["expected_verdict"]
    mark = f"{C['g']}✓ مطابق للمتوقع{C['0']}" if ok else \
           f"{C['r']}✗ توقعنا {sc['expected_verdict']}{C['0']}"
    print(f"\n  {mark}")
    return ok


def _wrap(text: str, width: int) -> list[str]:
    out, line = [], ""
    for word in text.split():
        if len(line) + len(word) + 1 > width:
            out.append(line)
            line = word
        else:
            line = f"{line} {word}".strip()
    if line:
        out.append(line)
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("which", nargs="?", help="رقم السيناريو 1-3")
    ap.add_argument("--override", help="اسم الاستشاري المعتمِد")
    args = ap.parse_args()

    files = sorted(settings.scenarios_dir.glob("sc-*.json"))
    if args.which:
        files = [f for f in files if f.stem.endswith(args.which.zfill(2))]
        if not files:
            sys.exit(f"لا يوجد سيناريو بالرقم {args.which}")

    print(f"\n{C['B']}صِمَام — بوابة امتثال الأجهزة الطبية{C['0']}")
    print(f"{C['y']}⚠️  بيانات محاكاة لأغراض الهاكاثون فقط{C['0']}")

    s = Samaam()
    results = [run_one(s, json.loads(f.read_text()), args.override) for f in files]

    print()
    rule("━")
    print(f"{C['B']}سجل التدقيق{C['0']}")
    for a in s.audit_trail():
        print(f"  {C['d']}{a['at'][:19]}{C['0']}  {a['event']:<26} "
              f"{a['worklist_id']:<14} {C['d']}{a['actor']}{C['0']}")
    rule("━")
    good = sum(results)
    tone = C["g"] if good == len(results) else C["r"]
    print(f"{tone}{good}/{len(results)} سيناريو طابق المتوقع{C['0']}\n")


if __name__ == "__main__":
    main()
