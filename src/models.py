
def filter_out(x):
    return ('._' in x) or (' ' in x)

  
def filter_out_table():
  filepath = '/teams/DSC180A_FA20_A00/b05vpnxray/data/unzipped'
  data = os.listdir(filepath)
  df = pd.DataFrame({"input": data})
  df['remove'] = df['input'].apply(filter_out)
  df = df[df['remove'] == False]
  df = df.drop(columns = ["remove"])
  df.reset_index(drop=True, inplace=True)
  return df


def classify_training(x):
  return ('novideo' in x) or ('browsing' in x) or ('internet' in x)
    

def table_output_col(df):  
  df['output'] = df['input'].apply(classify_training).replace({True: 'Not Streaming', False: 'Streaming'})
  
def build_df(df):
  ft1 = []
  ft2 = []
  ft3 = []
  ft4 = []

  for i in range(len(df['input'])):
      fts = classifier(df['input'][i])

      ft1.append(fts[0])
      ft2.append(fts[1])
      ft3.append(fts[2])
      ft4.append(fts[3])


  df['feature1'] = ft1
  df['feature2'] = ft2
  df['feature3'] = ft3
  df['feature4'] = ft4
  
  
def build_model(df):
    
  X = df.drop(columns = ["output", 'input'])
  y = df['output']

  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)
  reg = LogisticRegression(random_state=0).fit(X, y)
