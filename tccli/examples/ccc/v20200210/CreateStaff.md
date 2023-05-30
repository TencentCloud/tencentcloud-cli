**Example 1: 创建客服示例**

创建客服示例

Input: 

```
tccli ccc CreateStaff --cli-unfold-argument  \
    --Staffs.0.Phone 联系电话 \
    --Staffs.0.Mail 联系人邮箱 \
    --Staffs.0.StaffNumber 001 \
    --Staffs.0.Name 小军 \
    --SdkAppId 1400000000
```

Output: 
```
{
    "Response": {
        "RequestId": "6bb56a09-2787-40bc-80c5-dc6dab783eff",
        "ErrorStaffList": null
    }
}
```

