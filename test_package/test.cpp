#include <iostream>
#include <meteoio/MeteoIO.h>


int main (void) {
    double Rh = 70;
    double Ta = -15;
    double Td = mio::Atmosphere::RhtoDewPoint(Rh/100.0,Ta+273.15,false);
    printf ("Td = %g\n", Td);
    return 0;
}
