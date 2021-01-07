**Example 1: 一键开启和关闭**



Input: 

```
tccli cfw ModifyAllSwitchStatus --cli-unfold-argument  \
    --Status 0 \
    --Type 2 \
    --ChangeType 3 \
    --Area ap-shanghai
```

Output: 
```
{
    "Response": {
        "Status": 0,
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

