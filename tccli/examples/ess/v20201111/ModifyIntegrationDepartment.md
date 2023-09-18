**Example 1: 更新企业部门信息**

更新部门ID对应部门的部门名称、客户系统部门ID和排序号。

Input: 

```
tccli ess ModifyIntegrationDepartment --cli-unfold-argument  \
    --Operator.UserId yDwgKUUcXXXXXXXXXXXXQZDRuD \
    --DeptName 运营部 \
    --DeptId yDwgIUUckp1gXXXXXXXXE8xOm12b9 \
    --DeptOpenId open_dept1 \
    --OrderNo 1
```

Output: 
```
{
    "Response": {
        "RequestId": "072125ef-xxxx-xxxx-xxxx-xxxxxx45dab9"
    }
}
```

**Example 2: 错误示例-参数不合法**

在使用此接口时，需要按照入参描述进行相应的设置，以确保参数的合法性。如果参数设置不合法，此接口将返回错误信息。
1. 客户系统部门ID超过限制长度（64字符）

Input: 

```
tccli ess ModifyIntegrationDepartment --cli-unfold-argument  \
    --Operator.UserId yDwgKUUcXXXXXXXXXXXXQZDRuD \
    --DeptName 运营部 \
    --DeptId yDwgIUUckp1gXXXXXXXXE8xOm12b9 \
    --DeptOpenId abcdefghijklmnopqrstuvwxyz-abcdefghijklmnopqrstuvwxyz-abcdefghijklmnopqrstuvwxyz \
    --OrderNo 1
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameter.ParamError",
            "Message": "部门openId请控制在64个字符以内"
        },
        "RequestId": "072125ef-xxxx-xxxx-xxxx-xxxxxx45dab9"
    }
}
```

**Example 3: 错误示例-数据不存在**

在使用此接口时，请确认入参部门ID正确无误。如果参数设置不正确，此接口将返回错误信息。

Input: 

```
tccli ess ModifyIntegrationDepartment --cli-unfold-argument  \
    --Operator.UserId yDwgKUUcXXXXXXXXXXXXQZDRuD \
    --DeptName 运营部 \
    --DeptId yDwgIUUckp1gXXXXXXXXE8xOm12b9 \
    --DeptOpenId 1234 \
    --OrderNo 1
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameter.DataNotFound",
            "Message": "父部门不存在，请核对后重试"
        },
        "RequestId": "072125ef-xxxx-xxxx-xxxx-xxxxxx45dab9"
    }
}
```

