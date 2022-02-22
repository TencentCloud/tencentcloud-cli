**Example 1: 修改CC精准防护策略**



Input: 

```
tccli antiddos ModifyCCPrecisionPolicy --cli-unfold-argument  \
    --InstanceId bgpip-0000011x \
    --PolicyId ccPrecs-00000326 \
    --PolicyAction alg \
    --PolicyList.0.FieldType value \
    --PolicyList.0.FieldName cgi \
    --PolicyList.0.Value /cadwe \
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

