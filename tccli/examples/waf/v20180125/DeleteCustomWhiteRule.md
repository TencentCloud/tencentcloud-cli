**Example 1: 删除指定的精准白名单规则**



Input: 

```
tccli waf DeleteCustomWhiteRule --cli-unfold-argument  \
    --RuleId 1100000001 \
    --Domain waf.tencentcloudapi.com
```

Output: 
```
{
    "Response": {
        "RequestId": "5d207f4f-0d41-4f5d-bce2-0320090c98d8",
        "Success": {
            "Message": "Success",
            "Code": "Success"
        }
    }
}
```

