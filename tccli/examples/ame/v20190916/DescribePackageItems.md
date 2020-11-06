**Example 1: 查询曲库包已核验歌曲列表接口**



Input: 

```
tccli ame DescribePackageItems --cli-unfold-argument  \
    --OrderId xxx \
    --Offset xxx \
    --Length xxx
```

Output: 
```
{
    "Response": {
        "PackageItems": [
            {
                "ArtistName": "格子兮,willen",
                "AuthorizedArea": "CN",
                "Duration": "00:03:13",
                "Img": "http://csimage.tingmall.com/album/095/954833-JPG-600X600-ALBUM.jpg",
                "ItemID": "EB9DF7B88A3CF5BF5569BB40AF7AEF08",
                "OrderId": "00070710331231100",
                "TrackName": "十年寒冬"
            }
        ],
        "RequestId": "s1596078603574525000"
    }
}
```

