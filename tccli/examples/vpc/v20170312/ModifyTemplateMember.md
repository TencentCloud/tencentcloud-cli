**Example 1: 修改IP地址模板成员**



Input: 

```
tccli vpc ModifyTemplateMember --cli-unfold-argument  \
    --TemplateId ipm-test1234 \
    --OriginalTemplateMember.0.Member 10.0.0.1 \
    --OriginalTemplateMember.0.Description test \
    --OriginalTemplateMember.1.Member 172.20.0.1/24 \
    --TemplateMember.0.Member 10.0.0.2 \
    --TemplateMember.0.Description 'test modify' \
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
    --TemplateId ipmg-test1234 \
    --OriginalTemplateMember.0.Member ipm-test1234 \
    --OriginalTemplateMember.0.Description test \
    --OriginalTemplateMember.1.Member ipm-demo1234 \
    --TemplateMember.0.Member ipm-test5678 \
    --TemplateMember.0.Description 'test modify' \
    --TemplateMember.1.Member ipm-demo5678
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
    --TemplateId ppm-test1234 \
    --OriginalTemplateMember.0.Member TCP:80 \
    --OriginalTemplateMember.0.Description test \
    --OriginalTemplateMember.1.Member TCP:443 \
    --TemplateMember.0.Member TCP:8080 \
    --TemplateMember.0.Description 'test modify' \
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
    --TemplateId ppmg-test1234 \
    --OriginalTemplateMember.0.Member ppm-test1234 \
    --OriginalTemplateMember.0.Description test \
    --OriginalTemplateMember.1.Member ppm-demo1234 \
    --TemplateMember.0.Member ppm-test5678 \
    --TemplateMember.0.Description 'test modify' \
    --TemplateMember.1.Member ppm-demo5678
```

Output: 
```
{
    "Response": {
        "RequestId": "ba7c7681-e051-469a-b0fc-210a373490a4"
    }
}
```

