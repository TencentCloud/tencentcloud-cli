**Example 1: 添加白名单**



Input: 

```
tccli cwp ModifyBashPolicy --cli-unfold-argument  \
    --Policy.Enable 1 \
    --Policy.Name testbash \
    --Policy.BashAction 1 \
    --Policy.Level 0 \
    --Policy.Descript testbash \
    --Policy.Rule dGVzdCo \
    --Policy.Scope 3 \
    --Policy.White 1 \
    --Policy.DealOldEvents 0
```

Output: 
```
{
    "Response": {
        "RequestId": "ecf21829-71f7-4de6-86c8-6c73e575efbe"
    }
}
```

