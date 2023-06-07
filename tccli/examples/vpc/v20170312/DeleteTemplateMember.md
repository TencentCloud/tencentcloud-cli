**Example 1: 删除IP地址模板成员**

删除IP地址模板成员

Input: 

```
tccli vpc DeleteTemplateMember --cli-unfold-argument  \
    --TemplateId ipm-test1234 \
    --TemplateMember.0.Member 10.0.0.1 \
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

**Example 2: 删除IP地址组模板成员**

删除IP地址组模板成员

Input: 

```
tccli vpc DeleteTemplateMember --cli-unfold-argument  \
    --TemplateId ipmg-test1234 \
    --TemplateMember.0.Member ipm-test1234 \
    --TemplateMember.1.Member ipm-demo1234
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

添加协议端口模板成员

Input: 

```
tccli vpc DeleteTemplateMember --cli-unfold-argument  \
    --TemplateId ppm-test1234 \
    --TemplateMember.0.Member TCP:80 \
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

添加协议端口组模板成员

Input: 

```
tccli vpc DeleteTemplateMember --cli-unfold-argument  \
    --TemplateId ppmg-test1234 \
    --TemplateMember.0.Member ppm-test1234 \
    --TemplateMember.1.Member ppm-demo1234
```

Output: 
```
{
    "Response": {
        "RequestId": "ba7c7681-e051-469a-b0fc-210a373490a4"
    }
}
```

