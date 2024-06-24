**Example 1: ModifyConfig**

修改配置

Input: 

```
tccli camp ModifyConfig --cli-unfold-argument  \
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

**Example 2: modifyconfig修改配置**



Input: 

```
tccli camp ModifyConfig --cli-unfold-argument  \
    --ProjectID prj-xxxxxx \
    --ConfigName dsada \
    --ConfigType CONFIGMAP \
    --ConfigVersion 0.0.1 \
    --Description aaa
```

Output: 
```
{
    "Response": {
        "RequestId": "26ccfdd8-6d24-4236-9321-58d0467da44f"
    }
}
```

