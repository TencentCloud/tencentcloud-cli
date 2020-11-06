**Example 1: 状态机执行列表**



Input: 

```
tccli asw DescribeExecutions --cli-unfold-argument  \
    --StateMachineResourceName qrn:qcs:asw:ap-guangzhou:1300074211:http:json:flowmachine:bilibili-machine:bfhzs4j8 \
    --PageSize 100 \
    --PageIndex 1 \
    --FilterExecutionStatus INIT
```

Output: 
```
{
    "Response": {
        "Executions": [
            {
                "ExecutionResourceName": "qrn:qcs:asw:sh:1300074212:http:json:flowmachine:flowservicetest:bcrlj429",
                "Name": "",
                "StartDate": "20200718144016",
                "StopDate": "20200718151746",
                "StateMachineResourceName": "qrn:qcs:asw:sh:1300074211:http:json:flowmachine:flowservicetest:bcrlj428",
                "Status": "INIT"
            },
            {
                "ExecutionResourceName": "qrn:qcs:asw:sh:1300074211:execution:bcrlj428name-gadfaa-dhsrga",
                "Name": "name-gadfaa-dhsrga",
                "StartDate": "1595949070308",
                "StopDate": "0",
                "StateMachineResourceName": "qrn:qcs:asw:sh:1300074211:http:json:flowmachine:flowservicetest:bcrlj428",
                "Status": "INIT"
            },
            {
                "ExecutionResourceName": "qrn:qcs:asw:sh:1300074211:execution:bcrlj428bf25rh1ibf25rh1j-bf25rh1k-bf25rh1l-bf25rh1m",
                "Name": "bf25rh1ibf25rh1j-bf25rh1k-bf25rh1l-bf25rh1m",
                "StartDate": "1595949208853",
                "StopDate": "0",
                "StateMachineResourceName": "qrn:qcs:asw:sh:1300074211:http:json:flowmachine:flowservicetest:bcrlj428",
                "Status": "INIT"
            },
            {
                "ExecutionResourceName": "qrn:qcs:asw:sh:1300074211:execution:bcrlj428:bf25tfhlbf25th6b-bf25th6c-bf25th6d-bf25th6e",
                "Name": "bf25tfhlbf25th6b-bf25th6c-bf25th6d-bf25th6e",
                "StartDate": "1595949231671",
                "StopDate": "0",
                "StateMachineResourceName": "qrn:qcs:asw:sh:1300074211:http:json:flowmachine:flowservicetest:bcrlj428",
                "Status": "INIT"
            },
            {
                "ExecutionResourceName": "qrn:qcs:asw:sh:1300074211:execution:bcrlj428:bf264z61bf264z62-bf264z63-bf264z64-bf264z65",
                "Name": "bf264z61bf264z62-bf264z63-bf264z64-bf264z65",
                "StartDate": "1595949362952",
                "StopDate": "0",
                "StateMachineResourceName": "qrn:qcs:asw:sh:1300074211:http:json:flowmachine:flowservicetest:bcrlj428",
                "Status": "INIT"
            },
            {
                "ExecutionResourceName": "qrn:qcs:asw:sh:1300074211:execution:bcrlj428:bf2681ulbf2681um-bf2681un-bf2681uo-bf2681up",
                "Name": "bf2681ulbf2681um-bf2681un-bf2681uo-bf2681up",
                "StartDate": "1595949397912",
                "StopDate": "0",
                "StateMachineResourceName": "qrn:qcs:asw:sh:1300074211:http:json:flowmachine:flowservicetest:bcrlj428",
                "Status": "INIT"
            },
            {
                "ExecutionResourceName": "qrn:qcs:asw:sh:1300074211:execution:bcrlj428:bf26eu3kbf26eu3l-bf26eu3m-bf26eu3n-bf26eu3o",
                "Name": "bf26eu3kbf26eu3l-bf26eu3m-bf26eu3n-bf26eu3o",
                "StartDate": "1595949474267",
                "StopDate": "0",
                "StateMachineResourceName": "qrn:qcs:asw:sh:1300074211:http:json:flowmachine:flowservicetest:bcrlj428",
                "Status": "INIT"
            }
        ],
        "PageSize": 10,
        "PageIndex": 1,
        "TotalCount": 7,
        "RequestId": ""
    }
}
```

