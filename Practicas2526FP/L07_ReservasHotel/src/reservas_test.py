from reservas import *

def test_lee_reservas(reservas:list[Reserva])->None:
  print("\ntest_lee_reservas")
  print("Total reservas:",len(reservas))
  print ("Las tres primeras:")
  for r in reservas[:3]:
    print(r)
    
def test_total_facturado(reservas: list[Reserva],fecha_ini:date|None=None,fecha_fin: date|None=None)->None:
  print("\ntest_total_facturado")
  print(f"Total facturado entre {fecha_ini} y {fecha_fin}:\
 {total_facturado(reservas,fecha_ini,fecha_fin)}")
 
 #El resto de test para implementación del alumnado
   
  
if __name__=='__main__':
  reservas=lee_reservas("data/reservas.csv")
  test_lee_reservas(reservas)
  
# Las XXXXXXXXX hay que sustituirla por lo que corresponda
# segun sean los resultados esperados
  
  test_total_facturado(reservas)
  test_total_facturado(reservas,date(2022,2,1),XXXXXXXXX)
  test_total_facturado(reservas,XXXXXXXXX))
  test_total_facturado(reservas,None,XXXXXXXXX)
  
  # test_servicios_adicionales(reservas)
  
  # test_reservas_más_largas(reservas)
  
  # test_dni_por_tipo(reservas,"Piscina")
  
  # test_cliente_mayor_facturacion(reservas)
  # test_cliente_mayor_facturacion(reservas,{"Parking"})
  # test_cliente_mayor_facturacion(reservas,XXXXXXXXX)
  
  # test_promedios_dias_estancias_por_tipo(reservas)
  
  # test_reserva_más_barata_por_número_personas(reservas)
  # test_reserva_más_barata_por_número_personas(reservas,XXXXXXXXX)
  
  # test_reserva_más_cara_por_mes(reservas)
  
  # test_clientes_por_servicio(reservas,3)
  # test_clientes_por_servicio(reservas,4,XXXXXXXXX)

  