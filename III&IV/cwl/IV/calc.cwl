cwlVersion: v1.2
class: CommandLineTool
baseCommand: ["python", "/app/calc.py"]
hints:
  DockerRequirement:
    dockerPull: lukavasiljevic/cwl-python-env
inputs:
  dataset:
    type: File
    inputBinding:
      position: 1
  k:
    type: int
    inputBinding:
      position: 2


outputs:
  fold:
    type: string
    outputBinding:
     glob: res_string
     loadContents: true
     outputEval: $(self[0].contents)

stdout: res_string