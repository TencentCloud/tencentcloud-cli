**Example 1: 添加IP地址模板成员**



Input: 

```
tccli vpc AddTemplateMember --cli-unfold-argument  \
    --TemplateId ipm-88t6207k \
    --TemplateMember.0.Member 10.0.0.1 \
    --TemplateMember.0.Description demo \
    --TemplateMember.1.Member 172.20.0.1/24
```

Output: 
```
{
    "Response": {
        "RequestId": "ba7c7681-e051-469a-b0fc-210a373490a4"
    }
}
```

**Example 2: 添加IP地址组模板成员**



Input: 

```
tccli vpc AddTemplateMember --cli-unfold-argument  \
    --TemplateId ipmg-dih8xdbq \
    --TemplateMember.0.Member ipm-88t6207k \
    --TemplateMember.0.Description demo \
    --TemplateMember.1.Member ipm-mdunqeb6
```

Output: 
```
{
    "Response": {
        "RequestId": "ba7c7681-e051-469a-b0fc-210a373490a4"
    }
}
```

**Example 3: 添加协议端口模板成员**



Input: 

```
tccli vpc AddTemplateMember --cli-unfold-argument  \
    --TemplateId ppm-6zwa44xm \
    --TemplateMember.0.Member TCP:80 \
    --TemplateMember.0.Description demo \
    --TemplateMember.1.Member TCP:443
```

Output: 
```
{
    "Response": {
        "RequestId": "ba7c7681-e051-469a-b0fc-210a373490a4"
    }
}
```

**Example 4: 添加协议端口组模板成员**



Input: 

```
tccli vpc AddTemplateMember --cli-unfold-argument  \
    --TemplateId ppmg-ms7c7gcr \
    --TemplateMember.0.Member ppm-6zwa44xm \
    --TemplateMember.0.Description demo \
    --TemplateMember.1.Member ppm-4tw1bxlq
```

Output: 
```
{
    "Response": {
        "RequestId": "ba7c7681-e051-469a-b0fc-210a373490a4"
    }
}
```

