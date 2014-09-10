from phystricks import *
def ExoXLVL():
    pspict,fig = SinglePicture("ExoXLVL")

    x=var('x')
    dist=0.1
    l=2.5

    C1=Rectangle( Point(-l,l),Point(-dist,dist) )
    C2=Rectangle( Point(0,0),Point(l,l) )
    C3=Rectangle( Point(0,0),Point(-l,-l) )
    C4=Rectangle( Point(dist,-dist),Point(l,-l) )

    C1.parameters.color="blue"
    C2.parameters.color="red"
    C3.parameters.color="cyan"
    C4.parameters.color="green"

    C1.parameters.style="dashed"
    C2.parameters.style=C1.parameters.style
    C2.parameters.style=C1.parameters.style
    C4.parameters.style=C1.parameters.style

    a1=C1.center()
    a1.parameters.symbol=""
    a1.put_mark(0,0,"\( xy\)")
    a2=C2.center()
    a2.parameters.symbol=""
    a2.put_mark(0,0,"\( x-y\)")
    a3=C3.center()
    a3.parameters.symbol=""
    a3.put_mark(0,0,"\( x^2y\)")
    a4=C4.center()
    a4.parameters.symbol=""
    a4.put_mark(0,0,"\( x+y\)")


    pspict.axes.no_graduation()

    pspict.DrawGraphs(C1,C2,C3,C4,a1,a2,a3,a4)
    pspict.DrawDefaultAxes()
    pspict.dilatation(1)
    fig.conclude()
    fig.write_the_file()
