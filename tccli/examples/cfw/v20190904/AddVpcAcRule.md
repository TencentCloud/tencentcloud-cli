**Example 1: 添加VPC内网间规则示例1**

添加VPC内网间规则ip类型

Input: 

```
tccli cfw AddVpcAcRule --cli-unfold-argument  \
    --Rules.0.OrderIndex 1 \
    --Rules.0.SourceContent 192.168.1.10 \
    --Rules.0.DestContent 10.0.0.1 \
    --Rules.0.Protocol TCP \
    --Rules.0.Port 80 \
    --Rules.0.RuleAction log \
    --Rules.0.Description 搜索描述 \
    --Rules.0.EdgeId ALL \
    --Rules.0.SourceType net \
    --Rules.0.DestType net \
    --Rules.0.Enable true
```

Output: 
```
{
    "Response": {
        "RuleUuids": [
            8888
        ],
        "RequestId": "9a86c4e3-b926-4244-919b-aba9a7e82686"
    }
}
```

**Example 2: 添加VPC内网间规则2**

添加VPC内网间规则地址模版

Input: 

```
tccli cfw AddVpcAcRule --cli-unfold-argument  \
    --Rules.0.OrderIndex 1 \
    --Rules.0.SourceContent mb_1256532032_1666263807415 \
    --Rules.0.DestContent 192.168.1.2 \
    --Rules.0.Protocol TCP \
    --Rules.0.Port -1/-1 \
    --Rules.0.RuleAction accept \
    --Rules.0.Description 搜索描述 \
    --Rules.0.EdgeId ALL \
    --Rules.0.SourceType template \
    --Rules.0.DestType net \
    --Rules.0.Enable true
```

Output: 
```
{
    "Response": {
        "RuleUuids": [
            8888
        ],
        "RequestId": "9a86c4e3-b926-4244-919b-aba9a7e82686"
    }
}
```

