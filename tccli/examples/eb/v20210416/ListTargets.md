**Example 1: 获取目标列表**



Input: 

```
tccli eb ListTargets --cli-unfold-argument  \
    --EventBusId eb-l65vlc2 \
    --RuleId rule-fdltium8
```

Output: 
```
{
    "Response": {
        "RequestId": "03118ade-8de2-4514-af4b-b9a2f170ddd9",
        "Targets": [
            {
                "EventBusId": "eb-l65vlc2u",
                "RuleId": "rule-fdltium8",
                "TargetDescription": {
                    "ResourceDescription": "qcs::scf:ap-guanzhou:uin/3473058547:namespace/default/function/test/1"
                },
                "TargetId": "target-azwj7s7g",
                "Type": "scf",
                "EnableBatchDelivery": false,
                "BatchEventCount": 1,
                "BatchTimeout": 1
            },
            {
                "EventBusId": "eb-l65vlc2u",
                "RuleId": "rule-fdltium8",
                "TargetDescription": {
                    "ResourceDescription": "qcs::scf:ap-guanzhou:uin/3473058547:namespace/default/function/test/1"
                },
                "TargetId": "target-o5yx01oq",
                "Type": "scf",
                "EnableBatchDelivery": false,
                "BatchEventCount": 1,
                "BatchTimeout": 1
            },
            {
                "EventBusId": "eb-l65vlc2u",
                "RuleId": "rule-fdltium8",
                "TargetDescription": {
                    "ResourceDescription": "qcs::scf:ap-guanzhou:uin/3473058547:namespace/default/function/test/1"
                },
                "TargetId": "target-prp1ovqi",
                "Type": "scf",
                "EnableBatchDelivery": false,
                "BatchEventCount": 1,
                "BatchTimeout": 1
            },
            {
                "EventBusId": "eb-l65vlc2u",
                "RuleId": "rule-fdltium8",
                "TargetDescription": {
                    "ResourceDescription": "qcs::scf:ap-guanzhou:uin/3473058547:namespace/default/function/test/1"
                },
                "TargetId": "target-krcwchke",
                "Type": "scf",
                "EnableBatchDelivery": false,
                "BatchEventCount": 1,
                "BatchTimeout": 1
            },
            {
                "EventBusId": "eb-l65vlc2u",
                "RuleId": "rule-fdltium8",
                "TargetDescription": {
                    "ResourceDescription": "qcs::scf:ap-guanzhou:uin/3473058547:namespace/default/function/test/1"
                },
                "TargetId": "target-e9r3a1l0",
                "Type": "scf",
                "EnableBatchDelivery": false,
                "BatchEventCount": 1,
                "BatchTimeout": 1
            }
        ],
        "TotalCount": 5
    }
}
```

