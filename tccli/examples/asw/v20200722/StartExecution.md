**Example 1: 指定状态机启动执行**



Input: 

```
tccli asw StartExecution --cli-unfold-argument  \
    --StateMachineResourceName qrn:qcs:asw:ap-guangzhou:1300074211:http:json:flowmachine:bilibili-machine:bfhzs4j8 \
    --Input {"Bucket":"bilibili-1300074231","Region":"ap-shanghai","Object":"demo1.mp4"} \
    --Name thaf04gr-yjs96hs-fgjsfg464-u89yjfg5
```

Output: 
```
{
    "Response": {
        "ExecutionResourceName": "qrn:qcs:asw:ap-guangzhou:1300074211:execution:bfhzs4j8:bgi61l31bgi61l32-bgi61l33-bgi61kw0-bgi61kw1",
        "StartDate": "1596716960181",
        "RequestId": "hnr533hdf-yky4ye56-dhst6-jt7sdfgq552f"
    }
}
```

