**Example 1: 修改IP地址模板成员**



Input: 

```
tccli vpc ModifyTemplateMember --cli-unfold-argument  \
    --TemplateId ipm-h0fk8lfc \
    --OriginalTemplateMember.0.Member 10.0.0.1 \
    --OriginalTemplateMember.0.Description demo \
    --OriginalTemplateMember.1.Member 172.20.0.1/24 \
    --TemplateMember.0.Member 10.0.0.2 \
    --TemplateMember.0.Description demo \
    --TemplateMember.1.Member 192.168.0.1/24
```

Output: 
```
{
    "Response": {
        "RequestId": "ba7c7681-e051-469a-b0fc-210a373490a4"
    }
}
```

**Example 2: 修改IP地址组模板成员**



Input: 

```
tccli vpc ModifyTemplateMember --cli-unfold-argument  \
    --TemplateId ipmg-h0fk8lfc \
    --OriginalTemplateMember.0.Member ipm-hj3he929 \
    --OriginalTemplateMember.0.Description demo \
    --OriginalTemplateMember.1.Member ipm-nswq8wkq \
    --TemplateMember.0.Member ipm-pnpcflil \
    --TemplateMember.0.Description demo \
    --TemplateMember.1.Member ipm-4d8a10a1
```

Output: 
```
{
    "Response": {
        "RequestId": "ba7c7681-e051-469a-b0fc-210a373490a4"
    }
}
```

**Example 3: 修改协议端口模板成员**



Input: 

```
tccli vpc ModifyTemplateMember --cli-unfold-argument  \
    --TemplateId ppm-4d8a10a1 \
    --OriginalTemplateMember.0.Member TCP:80 \
    --OriginalTemplateMember.0.Description demo \
    --OriginalTemplateMember.1.Member TCP:443 \
    --TemplateMember.0.Member TCP:8080 \
    --TemplateMember.0.Description demo \
    --TemplateMember.1.Member TCP:6278
```

Output: 
```
{
    "Response": {
        "RequestId": "ba7c7681-e051-469a-b0fc-210a373490a4"
    }
}
```

**Example 4: 修改协议端口组模板成员**



Input: 

```
tccli vpc ModifyTemplateMember --cli-unfold-argument  \
    --TemplateId ppmg-hj3he929 \
    --OriginalTemplateMember.0.Member ppm-4d8a10a1 \
    --OriginalTemplateMember.0.Description demo \
    --OriginalTemplateMember.1.Member ppm-pnpcflil \
    --TemplateMember.0.Member ppm-4d8a10a1 \
    --TemplateMember.0.Description demo \
    --TemplateMember.1.Member ppm-4t7fr3fi
```

Output: 
```
{
    "Response": {
        "RequestId": "ba7c7681-e051-469a-b0fc-210a373490a4"
    }
}
```

