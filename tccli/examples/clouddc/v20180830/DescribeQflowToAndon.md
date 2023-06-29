**Example 1: 交付中心与安灯对接接口**

交付中心项目在andon 创建工单时需要获取更全面的项目信息， 客户信息。
https://iwiki.oa.tencent.com/pages/viewpage.action?pageId=268808245

Input: 

```
tccli clouddc DescribeQflowToAndon --cli-unfold-argument  \
    --LtcId 2018091401522
```

Output: 
```
{
    "Response": {
        "RequestId": "12345",
        "JsonData": "[{\"ltc_id\":\"2018070901321\",\"project_name\":\"\\u6d77\\u901a\\u8bc1\\u5238\\u4eba\\u5de5\\u667a\\u80fd\\u949b\\u5e73\\u53f0\\u9879\\u76ee\",\"children\":[{\"ltc_id\":\"2018070901321\",\"order_id\":\"TE375312019-04-15\",\"project_name\":\"\\u6d77\\u901a\\u8bc1\\u5238\\u4eba\\u5de5\\u667a\\u80fd\\u949b\\u5e73\\u53f0\\u9879\\u76ee\",\"customer_cid\":\"55409d03885d1293680189b34cc18c84\",\"customer_uin\":\"1097352543\",\"customer_name\":\"\",\"server_provider\":\"\\u4e1c\\u533a-\\u817e\\u4e91\\u5fc6\\u60f3\",\"service_stage\":\"\\u96c6\\u6210\\u4ea4\\u4ed8\",\"service_type\":\"\\u4ea4\\u4ed8\\u5b9e\\u65bd\",\"product_name\":\"TI-ONE\",\"server_name\":\"\\u4ea4\\u4ed8\\u5de5\\u7a0b\\u5e08\",\"order_enter_date\":\"2019-04-15\",\"order_leave_date\":\"\\u65e0\",\"create_time\":\"2019-07-20 07:05:56\",\"project_trade\":\"\\u91d1\\u878d\",\"region\":\"\\u534e\\u4e1c\",\"region_id\":4,\"region_spm\":\"tomtliang\",\"region_technology_spmo\":\"\",\"department\":\"\\u667a\\u6167\\u884c\\u4e1a5\\u90e8\\u91d1\\u878d\",\"game_point\":\"\",\"deliver_version\":\"\"},{\"ltc_id\":\"2018070901321\",\"order_id\":\"TE375282019-04-15\",\"project_name\":\"\\u6d77\\u901a\\u8bc1\\u5238\\u4eba\\u5de5\\u667a\\u80fd\\u949b\\u5e73\\u53f0\\u9879\\u76ee\",\"customer_cid\":\"55409d03885d1293680189b34cc18c84\",\"customer_uin\":\"1097352543\",\"customer_name\":\"\",\"server_provider\":\"\\u4e1c\\u533a-\\u817e\\u4e91\\u5fc6\\u60f3\",\"service_stage\":\"\\u96c6\\u6210\\u4ea4\\u4ed8\",\"service_type\":\"\\u4ea4\\u4ed8\\u5b9e\\u65bd\",\"product_name\":\"TI-ONE\",\"server_name\":\"\\u4ea4\\u4ed8\\u5de5\\u7a0b\\u5e08\",\"order_enter_date\":\"2019-04-10\",\"order_leave_date\":\"2019-08-31\",\"create_time\":\"2019-07-20 06:58:02\",\"project_trade\":\"\\u91d1\\u878d\",\"region\":\"\\u534e\\u4e1c\",\"region_id\":4,\"region_spm\":\"tomtliang\",\"region_technology_spmo\":\"\",\"department\":\"\\u667a\\u6167\\u884c\\u4e1a5\\u90e8\\u91d1\\u878d\",\"game_point\":\"\",\"deliver_version\":\"\"}]}]"
    }
}
```

