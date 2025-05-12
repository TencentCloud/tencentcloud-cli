**Example 1: 成功更新代码模版**

成功更新代码模版

Input: 

```
tccli wedata UpdateCodeTemplate --cli-unfold-argument  \
    --ProjectId 1470547050521227264 \
    --CodeTemplateId 20250319120202893 \
    --CodeTemplateName dfa \
    --InChargeId 100028579606 \
    --InCharge wenjieyao \
    --Ext.Properties.0.ParamKey bucket \
    --Ext.Properties.0.ParamValue wedata-fusion-dev-1257305158 \
    --Ext.Properties.1.ParamKey ftp.file.name \
    --Ext.Properties.1.ParamValue https://wedata-fusion-dev-1257305158.cos.ap-nanjing.myqcloud.com/datastudio/codeTemplate/1470547050521227264/dfa.py \
    --Ext.Properties.2.ParamKey region \
    --Ext.Properties.2.ParamValue ap-nanjing \
    --BrokerIp any \
    --ResourceGroup 20240222212719833743 \
    --CodeTemplateDesc 343 \
    --RequestFromSource WEB \
    --ScriptChange True
```

Output: 
```
{
    "Response": {
        "Data": true,
        "RequestId": "2430cabe-8dca-455e-917f-b86c78477e10"
    }
}
```

