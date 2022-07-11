**Example 1: 上报用户画像**



Input: 

```
tccli irp ReportPortrait --cli-unfold-argument  \
    --Bid deeb213e_d5a8 \
    --PortraitList.0.LastModifyTimestamp 1639624786 \
    --PortraitList.0.ResidentCity 深圳 \
    --PortraitList.0.ResidentDistrict 南山 \
    --PortraitList.0.Occupation 程序员 \
    --PortraitList.0.MembershipLevel 高 \
    --PortraitList.0.DislikeInfoList.0.Type authorId \
    --PortraitList.0.DislikeInfoList.0.Value 122 \
    --PortraitList.0.DislikeInfoList.1.Type authorId \
    --PortraitList.0.DislikeInfoList.1.Value 125 \
    --PortraitList.0.LastLoginIp 127.0.0.1 \
    --PortraitList.0.UserIdList.0.UserIdType 1 \
    --PortraitList.0.UserIdList.0.UserId 412323 \
    --PortraitList.0.UserIdList.1.UserIdType 4 \
    --PortraitList.0.UserIdList.1.UserId 9994f7wqeqweb88365e0f773dc81cec186 \
    --PortraitList.0.TagInfoList.0.Id 1231 \
    --PortraitList.0.TagInfoList.0.Name tag1231 \
    --PortraitList.0.TagInfoList.0.Weight 123.31 \
    --PortraitList.0.TagInfoList.1.Id 1232 \
    --PortraitList.0.TagInfoList.1.Name tag1232 \
    --PortraitList.0.TagInfoList.1.Weight 123.32 \
    --PortraitList.0.ResidentProvince 广东 \
    --PortraitList.0.LastLoginTimestamp 1639624786 \
    --PortraitList.0.RegisterTimestamp 1639624786 \
    --PortraitList.0.ResidentCountry CN \
    --PortraitList.0.Degree 大学 \
    --PortraitList.0.PhoneMd5 dahwiuhdaw \
    --PortraitList.0.School xx大学 \
    --PortraitList.0.Extension {} \
    --PortraitList.0.Oaid dhawhdiawhui \
    --PortraitList.0.Idfa dhawhdiawhui \
    --PortraitList.0.AndroidId dhawhdiawhui \
    --PortraitList.0.Gender 1 \
    --PortraitList.0.Age 22 \
    --PortraitList.0.AppId 12345678901 \
    --PortraitList.0.PhoneImei dhawidhjoahwfoaw \
    --PortraitList.0.AuthorInfoList.0.SourceId 1 \
    --PortraitList.0.AuthorInfoList.0.Id 123 \
    --PortraitList.0.AuthorInfoList.0.FollowType 1 \
    --PortraitList.0.AuthorInfoList.0.Name 1231 \
    --PortraitList.0.AuthorInfoList.0.IconUrl http://xx.jpg \
    --PortraitList.0.AuthorInfoList.1.SourceId 1 \
    --PortraitList.0.AuthorInfoList.1.Id 124 \
    --PortraitList.0.AuthorInfoList.1.FollowType 2 \
    --PortraitList.0.AuthorInfoList.1.Name 1234 \
    --PortraitList.0.AuthorInfoList.1.IconUrl http://xx.jpg \
    --PortraitList.0.Industry 互联网
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

