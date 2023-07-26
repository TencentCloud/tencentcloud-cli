**Example 1: CreateConfig**

创建配置

Input: 

```
tccli camp CreateConfig --cli-unfold-argument  \
    --Platform abc \
    --ProjectID abc \
    --ConfigName abc \
    --ConfigVersion abc \
    --ConfigType abc \
    --Content.ConfigMap.TypeMeta.APIVersion abc \
    --Content.ConfigMap.TypeMeta.Kind abc \
    --Content.ConfigMap.ObjectMeta.Name abc \
    --Content.ConfigMap.ObjectMeta.Namespace abc \
    --Content.ConfigMap.ObjectMeta.Labels.0.Key abc \
    --Content.ConfigMap.ObjectMeta.Labels.0.Value abc \
    --Content.ConfigMap.ObjectMeta.Annotations.0.Key abc \
    --Content.ConfigMap.ObjectMeta.Annotations.0.Value abc \
    --Content.ConfigMap.Immutable True \
    --Content.ConfigMap.Data.0.Key abc \
    --Content.ConfigMap.Data.0.Value abc \
    --Content.Secret.TypeMeta.APIVersion abc \
    --Content.Secret.TypeMeta.Kind abc \
    --Content.Secret.ObjectMeta.Name abc \
    --Content.Secret.ObjectMeta.Namespace abc \
    --Content.Secret.Immutable True \
    --Content.Secret.Type abc \
    --Content.Raw abc \
    --Description abc
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

