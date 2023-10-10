**Example 1: 示例**



Input: 

```
tccli cwp DescribeFastAnalysis --cli-unfold-argument  \
    --To 1657511824000 \
    --FieldName cls_event_type \
    --From 1657468800000 \
    --Query 
```

Output: 
```
{
    "Response": {
        "FieldValueRatioInfos": [
            {
                "Count": 56412,
                "Ratio": 0.59550929493608,
                "Value": "malware"
            },
            {
                "Count": 27836,
                "Ratio": 0.29384876859251,
                "Value": "asset_package"
            },
            {
                "Count": 2291,
                "Ratio": 0.024184779740101,
                "Value": "asset_core_module"
            },
            {
                "Count": 1873,
                "Ratio": 0.019772192253692,
                "Value": "asset_init_service"
            },
            {
                "Count": 1797,
                "Ratio": 0.0189699036198,
                "Value": "asset_env"
            },
            {
                "Count": 1506,
                "Ratio": 0.015897982666343,
                "Value": "asset_account"
            },
            {
                "Count": 1375,
                "Ratio": 0.014515090415818,
                "Value": "asset_jar"
            },
            {
                "Count": 390,
                "Ratio": 0.0041170074633956,
                "Value": "asset_netstat"
            },
            {
                "Count": 351,
                "Ratio": 0.003705306717056,
                "Value": "asset_app"
            },
            {
                "Count": 332,
                "Ratio": 0.0035047345585829,
                "Value": "asset_scheduled_task"
            }
        ],
        "RequestId": "6b4fc486-f623-4d19-bbc8-14c2396d7cc3",
        "TotalCount": 10
    }
}
```

