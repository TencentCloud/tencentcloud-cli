**Example 1: 查询运行参数模板内容**



Input: 

```
tccli omics GetInputTemplateFile --cli-unfold-argument  \
    --InputTemplateId in-slow-cerulean-anchovy-423943 \
    --ProjectId prj-best-orange-squid-853353
```

Output: 
```
{
    "Response": {
        "Content": "{\"FastpDemo.in1\":\"cos://*******************************************************************************************\",\"FastpDemo.in2\":\"cos://****-**************************************************************************************\",\"FastpDemo.RunFastp.json\":\"fastp.json\",\"FastpDemo.RunFastp.html\":\"fastp.html\",\"FastpDemo.RunFastp.report_title\":\"fastp report\"}",
        "CosSignedUrl": "https://genomics-*********************************************s/10*0**14*8*1*p***************-**********id***********l*ca**o**a****************************-**********u*/**-*******r***********************put.json?q-sign-algorithm=sha*****************2***************************-**gn-*i*e********0**********************t**e*1*7*6*6**9*********************************************************a*********42**8*******************7**********1",
        "RequestId": "ed9a3e8a-4f5c-432b-b44a-6cc562080b5c"
    }
}
```

