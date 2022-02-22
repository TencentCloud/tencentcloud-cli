**Example 1: 新增CC精准防护策略**



Input: 

```
tccli antiddos CreateCCPrecisionPolicy --cli-unfold-argument  \
    --InstanceId bgpip-0000011x \
    --Ip 1.2.1.3 \
    --Protocol HTTP \
    --Domain 1.acx.com \
    --PolicyAction alg \
    --PolicyList.0.FieldType value \
    --PolicyList.0.FieldName cgi \
    --PolicyList.0.Value /asd \
    --PolicyList.0.ValueOperator equal
```

Output: 
```
{
    "Response": {
        "RequestId": "5063ab0a-a8a7-41e8-ace2-263b2c1c8794"
    }
}
```

