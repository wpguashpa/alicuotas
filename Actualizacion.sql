
update [REMATES_JUDICIALES].[dbo].[polls_ad] set 
[calculated_appraisal_decimal] =cast(rtrim(Ltrim(REPLACE(SUBSTRING( [calculated_appraisal],0, CHARINDEX(' ' , [calculated_appraisal])), ',', ''))) as numeric(18,2)),
[expert_appraisal_decimal] = cast(rtrim(Ltrim(REPLACE([expert_appraisal], ',', ''))) as numeric(18,2)),
[city] = SUBSTRING( location,0, CHARINDEX(CHAR(10) , location))