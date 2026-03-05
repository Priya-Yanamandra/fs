from app import predict_value

def test_prediction():
    assert round(predict_value(6)) == 12