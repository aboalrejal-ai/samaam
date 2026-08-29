import { useTranslation } from 'react-i18next'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import { Input } from '@/components/ui/input'
import { Label } from '@/components/ui/label'
import { Switch } from '@/components/ui/switch'
import { Measured } from '@/components/primitives'
import type { Patient, Requested } from '@/types/api'

/**
 * The technologist's inputs.
 *
 * The eGFR card is the largest value in this column because it is the fact
 * that decides the case, and it carries its provenance line: the service
 * computed it with the equation the MOH protocol prescribes. Nothing here
 * computes a threshold or predicts a verdict — that is the policy node's job,
 * and duplicating it in the browser would be a second source of truth.
 */
export interface RequestFormProps {
  patient: Patient
  requested: Requested
  disabled?: boolean
  onPatientChange: (patch: Partial<Patient>) => void
  onRequestedChange: (patch: Partial<Requested>) => void
}

function Field({ label, children }: { label: string; children: React.ReactNode }) {
  return (
    <div className="space-y-1.5">
      <Label className="text-xs text-muted-foreground">{label}</Label>
      {children}
    </div>
  )
}

export function RequestForm({
  patient, requested, disabled, onPatientChange, onRequestedChange,
}: RequestFormProps) {
  const { t } = useTranslation()
  const num = (value: string) => (value === '' ? null : Number(value))

  return (
    <div className="space-y-4">
      <Card>
        <CardHeader className="pb-3">
          <CardTitle className="text-base">{t('console.patient')}</CardTitle>
        </CardHeader>
        <CardContent className="space-y-3">
          <div className="grid grid-cols-3 gap-2">
            <Field label={t('console.age')}>
              <Input type="number" value={patient.age} disabled={disabled}
                onChange={(e) => onPatientChange({ age: Number(e.target.value) })} />
            </Field>
            <Field label={t('console.weight')}>
              <Input type="number" value={patient.weight_kg ?? ''} disabled={disabled}
                onChange={(e) => onPatientChange({ weight_kg: num(e.target.value) })} />
            </Field>
            <Field label={t('console.sex')}>
              <Input value={patient.sex} disabled={disabled}
                onChange={(e) => onPatientChange({ sex: e.target.value })} />
            </Field>
          </div>
          {patient.diagnosis && (
            <p className="text-sm text-fg-2">{patient.diagnosis}</p>
          )}
          {!!patient.medications?.length && (
            <div className="flex flex-wrap gap-1.5">
              {patient.medications.map((drug) => (
                <span key={drug}
                  className="rounded-pill border border-border bg-surface-warm px-2 py-0.5 text-xs text-fg-2">
                  {drug}
                </span>
              ))}
            </div>
          )}
        </CardContent>
      </Card>

      <Card>
        <CardHeader className="pb-3">
          <CardTitle className="text-base">{t('console.renal')}</CardTitle>
        </CardHeader>
        <CardContent className="space-y-3">
          <Field label={`${t('console.creatinine')} (µmol/L)`}>
            <Input type="number" value={patient.serum_creatinine_umol_l ?? ''} disabled={disabled}
              onChange={(e) => onPatientChange({ serum_creatinine_umol_l: num(e.target.value) })} />
          </Field>
          <div className="rounded-md border border-border bg-surface-warm px-3 py-2.5">
            <p className="text-xs text-muted-foreground">{t('console.egfr')}</p>
            {patient.egfr == null ? (
              <p className="pt-1 text-sm text-muted-foreground">{t('console.egfrPending')}</p>
            ) : (
              <Measured value={patient.egfr} unit="mL/min/1.73m²" size="lg" />
            )}
            <p className="pt-1 text-xs text-muted-foreground">{t('console.egfrProvenance')}</p>
          </div>
          <div className="flex items-center justify-between">
            <Label className="text-sm">{t('console.onMetformin')}</Label>
            <Switch checked={patient.on_metformin ?? false} disabled={disabled}
              onCheckedChange={(v) => onPatientChange({ on_metformin: v })} />
          </div>
        </CardContent>
      </Card>

      <Card>
        <CardHeader className="pb-3">
          <CardTitle className="text-base">{t('console.acquisition')}</CardTitle>
        </CardHeader>
        <CardContent className="grid grid-cols-2 gap-2">
          <Field label={t('console.bodyRegion')}>
            <Input value={requested.body_region} disabled={disabled}
              onChange={(e) => onRequestedChange({ body_region: e.target.value })} />
          </Field>
          <Field label={t('console.kvp')}>
            <Input type="number" value={requested.kvp ?? ''} disabled={disabled}
              onChange={(e) => onRequestedChange({ kvp: num(e.target.value) })} />
          </Field>
          <Field label={`${t('console.ctdivol')} (mGy)`}>
            <Input type="number" step="0.1" value={requested.ctdivol_mgy ?? ''} disabled={disabled}
              onChange={(e) => onRequestedChange({ ctdivol_mgy: num(e.target.value) })} />
          </Field>
          <Field label={`${t('console.dlp')} (mGy·cm)`}>
            <Input type="number" value={requested.dlp_mgy_cm ?? ''} disabled={disabled}
              onChange={(e) => onRequestedChange({ dlp_mgy_cm: num(e.target.value) })} />
          </Field>
        </CardContent>
      </Card>

      <Card>
        <CardHeader className="pb-3">
          <CardTitle className="text-base">{t('console.contrast')}</CardTitle>
        </CardHeader>
        <CardContent className="space-y-3">
          <div className="grid grid-cols-2 gap-2">
            <Field label={t('console.agent')}>
              <Input value={requested.contrast_agent ?? ''} disabled={disabled}
                onChange={(e) => onRequestedChange({ contrast_agent: e.target.value || null })} />
            </Field>
            <Field label={`${t('console.volume')} (mL)`}>
              <Input type="number" value={requested.volume_ml ?? ''} disabled={disabled}
                onChange={(e) => onRequestedChange({ volume_ml: num(e.target.value) })} />
            </Field>
          </div>
          <div className="flex items-center justify-between">
            <Label className="text-sm">{t('console.prophylaxisOrdered')}</Label>
            <Switch checked={requested.prophylaxis_ordered ?? false} disabled={disabled}
              onCheckedChange={(v) => onRequestedChange({ prophylaxis_ordered: v })} />
          </div>
          <div className="flex items-center justify-between">
            <Label className="text-sm">{t('console.metforminHeld')}</Label>
            <Switch checked={requested.metformin_held ?? false} disabled={disabled}
              onCheckedChange={(v) => onRequestedChange({ metformin_held: v })} />
          </div>
        </CardContent>
      </Card>
    </div>
  )
}
