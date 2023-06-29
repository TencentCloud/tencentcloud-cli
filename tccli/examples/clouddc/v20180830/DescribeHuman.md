**Example 1: 天途人力资源接口**

查询天途人力资源信息
https://iwiki.woa.com/pages/viewpage.action?pageId=847009213

Input: 

```
tccli clouddc DescribeHuman --cli-unfold-argument  \
    --Enterprise p_linzhongguang
```

Output: 
```
{
    "Response": {
        "RequestId": "111",
        "JsonData": "{\"TotalCount\":1,\"List\":[{\"workspace_id\":\"20418055\",\"JobName\":\"\\u4ea7\\u54c1\\u67b6\\u6784\\u5e08\",\"departments\":\"\\u534e\\u5357\\u6280\\u672f\\u652f\\u6301\\u7ec4\",\"name2\":\"\\u6797\\u4e2d\\u5e7f\",\"Personnelgender\":\"\\u7537\",\"Productorientation\":\"\\u901a\\u7528\\u7c7b\",\"time\":\"2020-01-02\",\"Method\":\"\\u5176\\u4ed6\",\"Phone_number\":\"13426275812\",\"Weixin_Account\":\"\",\"Account\":\"\",\"Level\":\"10\",\"CHANPIN\":\"[]\",\"Enterprise\":\"p_linzhongguang\",\"Incumbency\":\"\\u5728\\u804c\",\"base_land\":\"\\u5317\\u4eac-\\u5317\\u4eac\\u5e02\",\"label_job_front\":\"1.5\\u7ebf\",\"label_profession\":\"\\u653f\\u52a1\",\"region_level\":\"\",\"label_management\":\"\",\"a_order_list\":[],\"post_category\":\"\\u79c1\\u6709\\u5316\\u4ea7\\u54c1\\u80fd\\u529b\\u5efa\\u8bbe\",\"region\":\"\\u4e1c\\u533a\"}]}"
    }
}
```

