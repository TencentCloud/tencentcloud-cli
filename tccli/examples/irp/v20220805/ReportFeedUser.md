**Example 1: 上报信息流用户信息**



Input: 

```
tccli irp ReportFeedUser --cli-unfold-argument  \
    --InstanceId deeb213e_d5a8 \
    --FeedUserList.0.UserId 2824324234 \
    --FeedUserList.0.UserIdList.0.Type qq \
    --FeedUserList.0.UserIdList.0.Value 412323 \
    --FeedUserList.0.UserIdList.1.Type imei_md5 \
    --FeedUserList.0.UserIdList.1.Value 9994f7wqeqweb88365e0f773dc81cec186 \
    --FeedUserList.0.Tags 科技:娱乐 \
    --FeedUserList.0.DislikeInfoList.0.Type author \
    --FeedUserList.0.DislikeInfoList.0.Value 作者名 \
    --FeedUserList.0.DislikeInfoList.1.Type author \
    --FeedUserList.0.DislikeInfoList.1.Value 作者名 \
    --FeedUserList.0.Age 22 \
    --FeedUserList.0.Gender 1 \
    --FeedUserList.0.Degree 本科 \
    --FeedUserList.0.School xx大学 \
    --FeedUserList.0.Occupation 销售 \
    --FeedUserList.0.Industry 互联网 \
    --FeedUserList.0.ResidentCountry CN \
    --FeedUserList.0.ResidentProvince CN-GD \
    --FeedUserList.0.ResidentCity 444100 \
    --FeedUserList.0.RegisterTimestamp 1639624786 \
    --FeedUserList.0.MembershipLevel 高 \
    --FeedUserList.0.LastLoginTimestamp 1639624786 \
    --FeedUserList.0.LastLoginIp 127.0.0.1 \
    --FeedUserList.0.LastModifyTimestamp 1639624786 \
    --FeedUserList.0.Extension {}
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

