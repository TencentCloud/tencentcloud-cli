**Example 1: 切换高危命令规则状态**



Input: 

```
tccli cwp ModifyBashPolicyStatus --cli-unfold-argument  \
    --Enable 0 \
    --Id 100
```

Output: 
```
{
    "Response": {
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a"
    }
}
```

**Example 2: 设置策略不生效**



Input: 

```
tccli cwp ModifyBashPolicyStatus --cli-unfold-argument  \
    --Enable 0 \
    --Id 10006
```

Output: 
```
{
    "Response": {
        "RequestId": "18db3474-a2a2-4763-9e36-d1379a98194c"
    }
}
```

