cwlVersion: v1.2
class: Workflow
inputs:
 in_csv: File
 col_name: string
 tr_ratio: float

outputs:
  metrics:
   type: File
   outputSource: step2/output_metrics

steps:
 step1:
  run: step1.cwl
  in:
    csv_file: in_csv
    column_name: col_name
  out: [output_csv]

 step2:
  run: step2.cwl
  in:
   csv_file: step1/output_csv
   training_ratio: tr_ratio
  out: [output_metrics]