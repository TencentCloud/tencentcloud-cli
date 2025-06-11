# Release 3.0.1218.1

## DNSPod(dnspod) 版本：2021-03-23

### 第 53 次发布

发布时间：2025-06-12 01:29:18

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [DescribeDomainVipList](http://document.tencentcloudapi.woa.com/document/product/1427/87026)
* [DescribeVasList](http://document.tencentcloudapi.woa.com/document/product/1427/87025)

修改接口：

* [CreateSubdomainValidateTXTValue](http://document.tencentcloudapi.woa.com/document/product/1427/85413)

	* 新增出参：ParentDomain


新增数据结构：

* [PackageListItem](http://document.tencentcloudapi.woa.com/document/product/1427/56185#PackageListItem)
* [SecurityInfo](http://document.tencentcloudapi.woa.com/document/product/1427/56185#SecurityInfo)
* [VasListItem](http://document.tencentcloudapi.woa.com/document/product/1427/56185#VasListItem)



## iOA 零信任安全管理系统(ioa) 版本：2022-06-01

### 第 7 次发布

发布时间：2025-06-12 01:39:29

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateDLPRiskPersonDownloadTask](http://document.tencentcloudapi.woa.com/document/product/1794/86548)

	* 新增入参：DomainInstanceId

* [DescribeDLPRiskPersonDashboard](http://document.tencentcloudapi.woa.com/document/product/1794/86520)

	* 新增入参：DomainInstanceId

* [DescribeDLPRiskPersonList](http://document.tencentcloudapi.woa.com/document/product/1794/86518)

	* 新增入参：DomainInstanceId, Condition, BeginTime, EndTime, RulePayload

* [DescribeDeviceHardwareInfoList](http://document.tencentcloudapi.woa.com/document/product/1794/86973)

	* 新增入参：MidList

* [ExportDLPRiskPersonList](http://document.tencentcloudapi.woa.com/document/product/1794/86503)

	* 新增入参：DomainInstanceId


新增数据结构：

* [RiskReportCondition](http://document.tencentcloudapi.woa.com/document/product/1794/86648#RiskReportCondition)
* [RiskReportGroupCondition](http://document.tencentcloudapi.woa.com/document/product/1794/86648#RiskReportGroupCondition)

修改数据结构：

* [DescribeSoftwareInformationPageData](http://document.tencentcloudapi.woa.com/document/product/1794/86648#DescribeSoftwareInformationPageData)

	* <font color="#dd0000">**修改成员**：</font>Items, Page




## 云开发低码(lowcode) 版本：2021-01-08

### 第 25 次发布

发布时间：2025-06-12 01:49:01

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [UploadKnowledgeDocumentSet](http://document.tencentcloudapi.woa.com/document/product/1599/85859)

	* 新增入参：FileId


修改数据结构：

* [KnowledgeSet](http://document.tencentcloudapi.woa.com/document/product/1599/75496#KnowledgeSet)

	* 新增成员：TotalSize

* [SearchDocInfo](http://document.tencentcloudapi.woa.com/document/product/1599/75496#SearchDocInfo)

	* 新增成员：FileId

* [UploadKnowledgeDocumentSetRsp](http://document.tencentcloudapi.woa.com/document/product/1599/75496#UploadKnowledgeDocumentSetRsp)

	* 新增成员：FileId




