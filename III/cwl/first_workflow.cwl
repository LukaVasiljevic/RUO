cwlVersion: v1.2
class: Workflow
inputs:
 py_1: File
 py_2: File
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
    python_file: py_1
    csv_file: in_csv
    column_name: col_name
  out: [output_csv]

 step2:
  run: step2.cwl
  in:
   python_file: py_2
   csv_file: step1/output_csv
   training_ratio: tr_ratio
  out: [output_metrics]
