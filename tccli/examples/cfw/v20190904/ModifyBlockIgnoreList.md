**Example 1: 入侵防御-封禁列表/放通列表-增删改接口**

支持对封禁列表、放通列表如下操作： 批量增加封禁IP、放通IP/域名 批量删除封禁IP、放通IP/域名 批量修改封禁IP、放通IP/域名生效事件

Input: 

```
tccli cfw ModifyBlockIgnoreList --cli-unfold-argument  \
    --IOC.0.IP 192.168.1.1 \
    --IOC.0.Direction 1 \
    --IOC.0.Domain  \
    --RuleType 1 \
    --IocAction add \
    --StartTime 2021-04-16 18:01:09 \
    --EndTime 3000-01-01 00:00:00
```

Output: 
```
{
    "Response": {
        "ReturnCode": 0,
        "ReturnMsg": "success",
        "RequestId": "cd0e1fdf-157d-438c-9bc8-75925e5d4e20"
    }
}
```

