import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import mlflow
import mlflow.sklearn
import math 

def train():
    print("Loading data....")
    df=pd.read_csv("data/menu.csv")
    
    X= df[['total_fat','carbs','protein','sugar']]
    y=df['calories']
    
    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2, random_state=1)
    
    # 2. Setup MLflow Experiment
    mlflow.set_experiment("Calorie_Predictor_v1")
    
    with mlflow.start_run():
        print("Starting training...")
        
        params ={
            "n_estimators":100,
            "max_depth":10,
            "random_state":42
        }    
        
        # Train Model
        rf = RandomForestRegressor(**params)
        rf.fit(X_train, y_train)
        
        # Predict
        predictions = rf.predict(X_test)
        
        # Calculate Metrics
        mse = mean_squared_error(y_test, predictions)
        rmse = math.sqrt(mse)
        r2 = r2_score(y_test, predictions)
        
        print(f"Metrics: RMSE={rmse:.2f}, R2={r2:.2f}")
        
        # 3. Log everything to MLflow
        # Log parameters (what we configured)
        mlflow.log_params(params)
        
        # Log metrics (how it performed)
        mlflow.log_metric("rmse", rmse)
        mlflow.log_metric("r2", r2)
        
        # Log the actual model file so we can deploy it later
        mlflow.sklearn.log_model(rf, "random_forest_model")
        
        print("✅ Run complete. Model logged to MLflow.")

if __name__ == "__main__":
    train()