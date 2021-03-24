import math

h = 0
s = 0
v = 0

def RGBcal(r,g,b):
  r = r/255
  g = g/255
  b = b/255
#find cmax, cmin
  rgb = [r, g, b]
  cmax = max(rgb)
  cmin = min(rgb)
  return cmax, cmin

def HSVcal(cmax, cmin):
#calculate Hue value
  diff = cmax - cmin
  if cmax == b:
    h = (60 * ((r - g) / diff) + 240) % 360
  elif cmax == r:
    h = (60* ((g - b) / diff) + 360) % 360
  elif cmax == g:
    h = (60 * ((b - r) / diff) + 120) % 360
  else:
    h = 0

#calculate Saturation
  if cmax != 0:
    s = (diff/cmax) * 100
  else:
    s = 0

#calculate Value
  v = cmax * 100
  return h, s, v


#input r,g,b
r = int(input())
g = int(input())
b = int(input())

HSVcal
#print result
print(round(h, 0))
print(round(s, 1))
print(round(v, 1))