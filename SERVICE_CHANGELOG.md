# Release 3.0.1396.1

## 日志服务(cls) 版本：2020-10-16

### 第 144 次发布

发布时间：2026-04-03 01:13:20

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [ChatCompletions](http://document.tencentcloudapi.woa.com/document/product/614/88698)

	* 新增入参：Model, Messages, Stream, Metadata

	* 新增出参：Created, Usage, Id, Choices, Model


新增数据结构：

* [ChatUsage](http://document.tencentcloudapi.woa.com/document/product/614/56471#ChatUsage)
* [Choice](http://document.tencentcloudapi.woa.com/document/product/614/56471#Choice)
* [Delta](http://document.tencentcloudapi.woa.com/document/product/614/56471#Delta)
* [Message](http://document.tencentcloudapi.woa.com/document/product/614/56471#Message)
* [MetadataItem](http://document.tencentcloudapi.woa.com/document/product/614/56471#MetadataItem)
* [ToolCall](http://document.tencentcloudapi.woa.com/document/product/614/56471#ToolCall)
* [ToolCallFunction](http://document.tencentcloudapi.woa.com/document/product/614/56471#ToolCallFunction)



## 数据湖计算 DLC(dlc) 版本：2021-01-25

### 第 151 次发布

发布时间：2026-04-03 01:17:47

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [Filter](http://document.tencentcloudapi.woa.com/document/product/1342/53778#Filter)

	* 新增成员：Operator

	* <font color="#dd0000">**修改成员**：</font>Name, Values




## 凭据管理系统(ssm) 版本：2019-09-23

### 第 15 次发布

发布时间：2026-04-03 01:32:21

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateProductSecret](http://document.tencentcloudapi.woa.com/document/product/1140/58266)

	* 新增入参：AccountType




## 云开发 CloudBase(tcb) 版本：2018-06-08

### 第 36 次发布

发布时间：2026-04-03 01:33:09

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [CreateCustomLoginKey](http://document.tencentcloudapi.woa.com/document/product/876/89362)

新增数据结构：

* [EmailTemplateConfig](http://document.tencentcloudapi.woa.com/document/product/876/34822#EmailTemplateConfig)
* [HTTPServiceExtension](http://document.tencentcloudapi.woa.com/document/product/876/34822#HTTPServiceExtension)
* [HTTPServiceHeaderToAdd](http://document.tencentcloudapi.woa.com/document/product/876/34822#HTTPServiceHeaderToAdd)
* [HTTPServiceHeadersHandler](http://document.tencentcloudapi.woa.com/document/product/876/34822#HTTPServiceHeadersHandler)
* [LocalizedTemplate](http://document.tencentcloudapi.woa.com/document/product/876/34822#LocalizedTemplate)

修改数据结构：

* [EmailProviderConfig](http://document.tencentcloudapi.woa.com/document/product/876/34822#EmailProviderConfig)

	* 新增成员：TemplateConfig

* [HTTPServiceDomain](http://document.tencentcloudapi.woa.com/document/product/876/34822#HTTPServiceDomain)

	* 新增成员：Extension

* [HTTPServiceDomainParam](http://document.tencentcloudapi.woa.com/document/product/876/34822#HTTPServiceDomainParam)

	* 新增成员：Extension

* [HTTPServiceRoute](http://document.tencentcloudapi.woa.com/document/product/876/34822#HTTPServiceRoute)

	* 新增成员：Extension

* [HTTPServiceRouteParam](http://document.tencentcloudapi.woa.com/document/product/876/34822#HTTPServiceRouteParam)

	* 新增成员：Extension




## 边缘安全加速平台(teo) 版本：2022-09-01

### 第 73 次发布

发布时间：2026-04-03 01:36:31

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [DescribeSharedCNAME](http://document.tencentcloudapi.woa.com/document/product/1738/89364)
* [ModifySharedCNAME](http://document.tencentcloudapi.woa.com/document/product/1738/89363)

新增数据结构：

* [IPSSLConfig](http://document.tencentcloudapi.woa.com/document/product/1738/81211#IPSSLConfig)
* [IPSSLSetting](http://document.tencentcloudapi.woa.com/document/product/1738/81211#IPSSLSetting)
* [ReferenceHolder](http://document.tencentcloudapi.woa.com/document/product/1738/81211#ReferenceHolder)
* [SharedCNAMEInfo](http://document.tencentcloudapi.woa.com/document/product/1738/81211#SharedCNAMEInfo)



## 边缘安全加速平台(teo) 版本：2022-01-06



## 数据开发治理平台 WeData(wedata) 版本：2025-10-10

### 第 4 次发布

发布时间：2026-04-03 01:43:21

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [CheckTable](http://document.tencentcloudapi.woa.com/document/product/1607/89372)
* [CreateCatalog](http://document.tencentcloudapi.woa.com/document/product/1607/89371)
* [CreateSchema](http://document.tencentcloudapi.woa.com/document/product/1607/89370)
* [DownloadJobResult](http://document.tencentcloudapi.woa.com/document/product/1607/89373)
* [GetSchema](http://document.tencentcloudapi.woa.com/document/product/1607/89369)
* [GetTable](http://document.tencentcloudapi.woa.com/document/product/1607/89368)
* [ListCatalogNames](http://document.tencentcloudapi.woa.com/document/product/1607/89367)
* [ListSchemaNames](http://document.tencentcloudapi.woa.com/document/product/1607/89366)
* [ListTableNames](http://document.tencentcloudapi.woa.com/document/product/1607/89365)

新增数据结构：

* [CheckTableRsp](http://document.tencentcloudapi.woa.com/document/product/1607/88970#CheckTableRsp)
* [CreateCatalogRsp](http://document.tencentcloudapi.woa.com/document/product/1607/88970#CreateCatalogRsp)
* [CreateSchemaRsp](http://document.tencentcloudapi.woa.com/document/product/1607/88970#CreateSchemaRsp)
* [DownloadJobResultRsp](http://document.tencentcloudapi.woa.com/document/product/1607/88970#DownloadJobResultRsp)
* [GetSchemaRsp](http://document.tencentcloudapi.woa.com/document/product/1607/88970#GetSchemaRsp)
* [GetTableRsp](http://document.tencentcloudapi.woa.com/document/product/1607/88970#GetTableRsp)
* [JobAsyncFile](http://document.tencentcloudapi.woa.com/document/product/1607/88970#JobAsyncFile)
* [JobFileAccessAuth](http://document.tencentcloudapi.woa.com/document/product/1607/88970#JobFileAccessAuth)
* [ListCatalogNamesRsp](http://document.tencentcloudapi.woa.com/document/product/1607/88970#ListCatalogNamesRsp)
* [ListSchemaNamesRsp](http://document.tencentcloudapi.woa.com/document/product/1607/88970#ListSchemaNamesRsp)
* [ListTableNamesRsp](http://document.tencentcloudapi.woa.com/document/product/1607/88970#ListTableNamesRsp)
* [NameIdentifier](http://document.tencentcloudapi.woa.com/document/product/1607/88970#NameIdentifier)
* [ProxyColumn](http://document.tencentcloudapi.woa.com/document/product/1607/88970#ProxyColumn)
* [ProxyJobResultMeta](http://document.tencentcloudapi.woa.com/document/product/1607/88970#ProxyJobResultMeta)



## 数据开发治理平台 WeData(wedata) 版本：2025-08-06



## 数据开发治理平台 WeData(wedata) 版本：2021-08-20



