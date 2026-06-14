# =========================
# preprocess.py (FINAL BOOST)
# =========================

import pandas as pd
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from sklearn.feature_selection import VarianceThreshold
from sklearn.model_selection import train_test_split

# def map_attack(label):
#     dos = ['neptune','smurf','back','teardrop','pod','land']
#     probe = ['satan','ipsweep','nmap','portsweep']
#     r2l = ['guess_passwd','ftp_write','imap','phf','multihop','warezmaster','warezclient']
#     u2r = ['buffer_overflow','loadmodule','rootkit','perl']

#     if label == 'normal': return 'normal'
#     elif label in dos: return 'dos'
#     elif label in probe: return 'probe'
#     elif label in r2l: return 'r2l'
#     elif label in u2r: return 'u2r'
#     else: return 'other'


def load_and_preprocess():
    df = pd.read_csv("dataset/KDDTrain+.txt", header = None)
    columns = [
    'duration','protocol_type','service','flag','src_bytes',
    'dst_bytes','land','wrong_fragment','urgent','hot',
    'num_failed_logins','logged_in','num_compromised','root_shell',
    'su_attempted','num_root','num_file_creations','num_shells',
    'num_access_files','num_outbound_cmds','is_host_login',
    'is_guest_login','count','srv_count','serror_rate',
    'srv_serror_rate','rerror_rate','srv_rerror_rate',
    'same_srv_rate','diff_srv_rate','srv_diff_host_rate',
    'dst_host_count','dst_host_srv_count',
    'dst_host_same_srv_rate','dst_host_diff_srv_rate',
    'dst_host_same_src_port_rate','dst_host_srv_diff_host_rate',
    'dst_host_serror_rate','dst_host_srv_serror_rate',
    'dst_host_rerror_rate','dst_host_srv_rerror_rate',
    'label','difficulty'
    ]
    df.columns = columns
    
    #test = pd.read_csv("dataset/KDDTest+.txt", names=columns)

    #df = pd.concat([train, test])
    #df.drop("difficulty", axis=1, inplace=True)

    # df['label'] = df['label'].apply(map_attack)
    df['label'] = df['label'].apply(
        lambda x: 0 if x == 'normal' else 1
    )

    # Encode categorical
    for col in ["protocol_type", "service", "flag"]:
        df[col] = LabelEncoder().fit_transform(df[col])
        
    df.drop('difficulty', axis=1, inplace=True)
    
    # Encode label
    #le = LabelEncoder()
    #df['label'] = le.fit_transform(df['label'])

    # train = df.iloc[:len(train)]
    # test = df.iloc[len(train):]

    # X_train = train.drop("label", axis=1)
    # y_train = train["label"]

    # X_test = test.drop("label", axis=1)
    # y_test = test["label"]
    X = df.drop('label', axis=1)

    y = df['label']
    
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    # 🔥 Better scaling (important for XGBoost)
    # scaler = MinMaxScaler()
    # X_train = scaler.fit_transform(X_train)
    # X_test = scaler.transform(X_test)

    # 🔥 Remove useless features
    # selector = VarianceThreshold()
    # X_train = selector.fit_transform(X_train)
    # X_test = selector.transform(X_test)

    return X_train, X_test, y_train, y_test