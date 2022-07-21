from datetime import datetime, timezone

from sklearn.svm import SVC
from joblib import load
import tweepy
import pandas as pd


def get_prediction(AI : SVC, data_frame : pd.DataFrame):
    """
    Função que, dado um dataset e a IA, retorna se o usuário é um bot ou humano, 
    além da chance de acerto da resposta.
    """

    resp = AI.predict(data_frame)  # Faz a previsão -> Se é humano ou bot
    resp_percent = AI.predict_proba(data_frame)  # Diz a probabilidade estar certa.

    return resp, resp_percent


def load_AI(file_location : str) -> SVC:
    """
    Função para carregar a IA.
    """

    return load(file_location)


def account_age(date : datetime) -> int:
    """
    Função que define a idade da conta, em dias.
    """

    return (datetime.now(timezone.utc) - date).days


def transform_into_data(user: tweepy.models.User) -> pd.DataFrame:
    """
    Função que, dado um usuário do Twitter, retorna um Dataset para esse usuário.
    """

    user_data = pd.DataFrame()
    user_data['default_profile'] = [user.default_profile]
    user_data['default_profile_image'] = [user.default_profile_image]
    user_data['favourites_count'] = [user.favourites_count]
    user_data['followers_count'] = [user.followers_count]
    user_data['friends_count'] = [user.friends_count]
    user_data['geo_enabled'] = [user.geo_enabled]
    user_data['statuses_count'] = [user.statuses_count]
    user_data['verified'] = [user.verified]
    
    age_days = account_age(user.created_at)

    if age_days != 0:
        user_data['average_tweets_per_day'] = [user.statuses_count / age_days]
    else:
        user_data['average_tweets_per_day'] = user.statuses_count

    user_data['account_age_days'] = [age_days]
    user_data['is_Description_Null'] = [len(user.description) <= 3]
    user_data['Description_Lenght'] = [len(user.description)]
    user_data['Name_Lenght'] = [len(user.screen_name)]

    return user_data
