/* Calculo de porcentajes de poblacion vacunada */

WITH PopulationVsVacines (Jurisdiccion, PrimeraDosis, SegundaDosis, TotalVacunas, 
	Poblacion2020, PorcentajePrimeraDosis, PorcentajeSegundaDosis, PorcentajeTotal) as
	(SELECT vac.jurisdiccion_nombre, vac.primera_dosis_cantidad, vac.segunda_dosis_cantidad, 
	vac.primera_dosis_cantidad + vac.segunda_dosis_cantidad,
	pob.[2020],
	100 * vac.primera_dosis_cantidad / pob.[2020],
	100 * vac.segunda_dosis_cantidad / pob.[2020],
	100 * (vac.primera_dosis_cantidad + vac.segunda_dosis_cantidad) / pob.[2020]
FROM Covid19_Vacunas vac
JOIN Poblacion_Arg pob
	ON vac.jurisdiccion_nombre = pob.jurisdiccion)
SELECT *
FROM PopulationVsVacines

SELECT *
INTO PopulationVsVacines
FROM Covid19_Vacunas vac
INNER JOIN Poblacion_Arg pob
ON vac.jurisdiccion_nombre = pob.jurisdiccion

SELECT *
FROM PopulationVsVacines

ALTER TABLE PopulationVsVacines ALTER COLUMN primera_dosis_cantidad float
ALTER TABLE PopulationVsVacines ALTER COLUMN segunda_dosis_cantidad float
ALTER TABLE PopulationVsVacines ALTER COLUMN [2020] float

SELECT DISTINCT SUM(primera_dosis_cantidad) OVER(PARTITION BY jurisdiccion_nombre),
	SUM(segunda_dosis_cantidad) OVER(PARTITION BY jurisdiccion_nombre), jurisdiccion_nombre
FROM PopulationVsVacines

ALTER TABLE PopulationVsVacines ADD PrimeraDosis as SUM(primera_dosis_cantidad) OVER(PARTITION BY jurisdiccion_nombre),
	SegundaDOsis as SUM(segunda_dosis_cantidad) OVER(PARTITION BY jurisdiccion_nombre)

SELECT jurisdiccion_nombre, primera_dosis_cantidad, segunda_dosis_cantidad, 
	primera_dosis_cantidad + segunda_dosis_cantidad as TotalVacunas,
	[2020] as Poblacion2020,
	100 * primera_dosis_cantidad / [2020] as PorcentajePrimeraDosis,
	100 * segunda_dosis_cantidad / [2020] as PorcentajeSegundaDosis,
	100 * (primera_dosis_cantidad + segunda_dosis_cantidad) / [2020] as PorcentajeTotal
FROM PopulationVsVacines

SELECT jurisdiccion_nombre, primera_dosis_cantidad, segunda_dosis_cantidad, [2020] as Poblacion2020
INTO data_out
FROM PopulationVsVacines

SELECT *
FROM Covid_Arg..data_out

ALTER TABLE data_out ADD TotalVacunas as primera_dosis_cantidad + segunda_dosis_cantidad,
	PorcentajePrimeraDosis as 100 * primera_dosis_cantidad / Poblacion2020,
	PorcentajeSegundaDosis as 100 * segunda_dosis_cantidad / Poblacion2020,
	PorcentajeTotal as 100 * (primera_dosis_cantidad + segunda_dosis_cantidad) / Poblacion2020

SELECT *
FROM Covid_Arg..data_out

SELECT
	t.jurisdiccion_nombre, t.primera_dosis, t.segunda_dosis, 
	100 * primera_dosis / Poblacion2020 as porcentaje_primera_dosis,
	100 * segunda_dosis / Poblacion2020 as porcentaje_segunda_dosis,
	t.Poblacion2020
	FROM ( SELECT DISTINCT
	SUM(primera_dosis_cantidad) OVER(PARTITION BY jurisdiccion_nombre) as primera_dosis,
	SUM(segunda_dosis_cantidad) OVER(PARTITION BY jurisdiccion_nombre) as segunda_dosis, 
	jurisdiccion_nombre, Poblacion2020
	FROM Covid_Arg..data_out) t
	ORDER BY t.jurisdiccion_nombre