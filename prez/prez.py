model.add(Convolution2D(1, # filter r�tegek sz�ma
                        3, 3, # 3x3 kernel m�ret
                        strides=(1,1) # l�p�s
                        input_shape=image))

