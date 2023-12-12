# -*- coding: utf-8 -*-
from keras.models import Sequential, Model
from keras.layers import Convolution1D, MaxPooling1D, GlobalMaxPooling1D, Dense, Dropout, Flatten, Input, concatenate, Add,  BatchNormalization, Activation, Bidirectional, LSTM, GRU,TimeDistributed,AveragePooling1D,GlobalAveragePooling1D
from keras import regularizers
from tensorflow.keras.layers import Layer, InputSpec
from keras import initializers
from keras import backend as K


# DeepBind model
def DeepBind_K(shape = None, params = None, penalty = 0.005):
    model = Sequential()
    model.add(Convolution1D(filters=16, kernel_size=13, padding='same', activation='relu',
                kernel_regularizer=regularizers.l2(penalty),input_shape=shape))
    model.add(GlobalMaxPooling1D())
    model.add(Dense(units=32, activation='relu', kernel_regularizer=regularizers.l2(penalty)))
    model.add(Dropout(params['DROPOUT']))
    model.add(Dense(units=1))
    
    print (model.summary())
    return model


## shared hybrid model--CRPTS using DNA sequences and DNA shape features
def SharedDeepBindwithShape(shape1=None, shape2=None, params=None, penalty=0.005):
    digit_input = Input(shape=shape1)
    print (digit_input.shape)
    X = Convolution1D(16, 13, activation='relu', padding='same')(digit_input)


    X1  = MaxPooling1D(2, 2)(X)
    # print('X1', X1.shape)
    # out = Bidirectional(LSTM(64))(X1)
    out = LSTM(32)(X1)
    # print('X2', X2.shape)
    # out = Dense(16,activation='relu')(X2)

    # print('out',out.shape)
    # out = TimeDistributed(Dense((LSTM(64))))(digit_input)
    out = Dropout(0.2)(out)
    share_model = Model(digit_input, out)

    main_input = Input(shape=shape1, name='sequence')
    out_main = share_model(main_input)

    auxiliary_input = Input(shape=shape2, name='shape')
    auxiliary_conv1 = Convolution1D(4, 1, activation='relu', padding='same', name='shape_conv')(auxiliary_input)
    out_aux = share_model(auxiliary_conv1)

    concat = concatenate([out_main, out_aux], axis=-1)
    Y = BatchNormalization()(concat)
    Y = Dense(32, activation='relu', kernel_regularizer=regularizers.l2(penalty))(Y)
    Y = Dropout(params['DROPOUT'])(Y)
    output = Dense(1)(Y)

    model = Model(inputs=[main_input, auxiliary_input], outputs=output)
    print (model.summary())
    return model

###CRPT only using DNA sequences 
def Sharedmodelsequence(shape1=None, params=None, penalty=0.005):
    digit_input = Input(shape=shape1)
    print (digit_input.shape)
    X = Convolution1D(16, 13, activation='relu', padding='same')(digit_input)


    X1 = MaxPooling1D(2, 2)(X)
    out = LSTM(32)(X1)

    out = Dropout(0.2)(out)
    share_model = Model(digit_input, out)

    main_input = Input(shape=shape1, name='sequence')
    out_main = share_model(main_input)

    concat = out_main
    Y = BatchNormalization()(concat)
    Y = Dense(32, activation='relu', kernel_regularizer=regularizers.l2(penalty))(Y)
    # Y = Dropout(params['DROPOUT'])(Y)
    Y = Dropout(0.2)(Y)
    output = Dense(1)(Y)

    model = Model(inputs= main_input, outputs=output)
    print (model.summary())
    return model


# # build hybrid model---non shared model
# def DeepBindwithShape(shape1=None, shape2=None, params=None, penalty = 0.005):
#
#     main_input = Input(shape=shape1, name='sequence')
#     X = Convolution1D(16, 13, activation='relu', padding='same', name='seq_conv')(main_input)
#     X = GlobalMaxPooling1D()(X)
#
#     auxiliary_input = Input(shape=shape2, name='shape')
#     Y = Convolution1D(16, 13, activation='relu', padding='same', name='shape_conv')(auxiliary_input)
#     Y = GlobalMaxPooling1D()(Y)
#
#     concat = concatenate([X, Y], axis=-1)
#     output = Dense(32, activation='relu', kernel_regularizer=regularizers.l2(penalty))(concat)
#     output = Dropout(params['DROPOUT'])(output)
#     output = Dense(1)(output)
#
#     model = Model(inputs=[main_input, auxiliary_input], outputs=output)
#     print (model.summary())
#     return model
 
# build other models
def DeepCNN(shape = None, params = None, penalty = 0.005):
    model = Sequential()
    model.add(Convolution1D(16, 13, activation='relu', padding='same', input_shape=shape))
    model.add(MaxPooling1D(2, 2))
    model.add(Dropout(0.2))
    model.add(Convolution1D(32, 7, activation='relu', padding='same'))
    model.add(MaxPooling1D(2, 2))
    model.add(Dropout(0.2))
    model.add(Convolution1D(32, 5, activation='relu', padding='same'))
    model.add(GlobalMaxPooling1D())
    model.add(Dense(32, activation='relu', kernel_regularizer=regularizers.l2(penalty)))
    model.add(Dropout(params['DROPOUT']))
    model.add(Dense(1))
    
    print (model.summary())
    return model


