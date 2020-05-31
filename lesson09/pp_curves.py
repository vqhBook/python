from figures import polar_para_curve as ppcur

ppcur(lambda t: 250, lambda t: t, 0, 360,
      50, line_color="red")
ppcur(lambda t: 0.15*t, lambda t: t, 0, 4*360,
      4*50, line_color="blue")
