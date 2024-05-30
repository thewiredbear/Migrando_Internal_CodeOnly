from pydantic import BaseModel




class RequestBody(BaseModel):
    Abschluss: str
    Abschluss_in_DE: str
    Deutscher_Ehepartner: str
    EB_NE_erfllt: str
    Einreisejahr: str
    Antrag_EB: str
    Antrag_NE: str
    Integrationstest: str
    Jahr_AR_beantragt_bekommen: str
    Jobcenter: str
    Kinder: int
    Netto: str
    Rente: str
    Sprachzertifikat: str
    Test_Sprache: str
    Welches_befristete_AR_haben_Sie: str
    Wie_ist_ihr_aktueller_Familienstand: str
    Beratung: str
    Gltiger_Nationalpass: str
    Id: str
    Zeitpunkt_der_Erstellung: str
    Sales: int
    Zeitpunkt_der_nderung: str
    Zeitpunkt_der_Erstellung_Year: int
    Zeitpunkt_der_nderung_Year: int
    SalesCount: int