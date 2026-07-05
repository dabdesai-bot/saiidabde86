import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
from sklearn.preprocessing import StandardScaler

def MarvellousClassifier(DataPath):
    Border="-"*40
    print(Border)

    #Step 1:Load the Dataset from csv
    print("Step 1:Load the Dataset from csv")
    print(Border)
    df =pd.read_csv(DataPath)
    print("Some Enteries from dataset")
    print(df.head())
    print(Border)

    #step 2: clean the dataset by removing empty data set
    print(Border)
    print("Step 2:clean the dataset by removing empty data set")
    print(Border) 
    df.dropna(inplace=True)
    print("Total Records:",df.shape[0])
    print("Total Columns:",df.shape[1])
    print(Border)

    #step 3: Seperate Independent and Dependent Variable
    print(Border)
    print("Step 3:Seperate Independent and Dependent Variable")
    print(Border) 
    X=df.drop(columns=['Class'])
    Y=df['Class']
    print("Shape of X:",X.shape)
    print("Shape of Y:",Y.shape)
    print(Border)
    print("Input Columns:",X.columns.tolist())
    print("Output list:Class")

    #step 4: Split The dataset for training and testing
    print(Border)
    print("Step 4:Split the dataset for training and testing")
    print(Border) 
    X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=42,stratify=Y)
    print(Border)
    print("Information of training and testing data")
    print("X_train shape:",X_train.shape)
    print("X_test shape:",X_test.shape)
    print("Y_train shape:",Y_train.shape)
    print("Y_test shape:",Y_test.shape)

    #step 5:Feature scaling 
    print(Border)
    print("Step 5:Feature Scaling")
    print(Border) 
    scalar=StandardScaler()
    #independent variable scaling
    X_train_scaled=scalar.fit_transform(X_train)
    X_test_scaled=scalar.fit_transform(X_test)
    print("Feature scaling is done")

    #step 6:Explore the multivalue of K
    #Hyperparameter tuning (k)

    accuracy_scores=[]
    K_values=range(1,21)

    for k in K_values:
        model=KNeighborsClassifier(n_neighbors=k)
        model.fit(X_train_scaled,Y_train)
        Y_pred=model.predict(X_test_scaled)
        accuracy=accuracy_score(Y_test,Y_pred)
        accuracy_scores.append(accuracy)
    print(Border)
    print("Accuracy report of all K values from 1 to 20")
    for value in accuracy_scores:
        print(value)
    print(Border)

    #Step 7: Plot graph of K Vs Accuracy
    print(Border)
    print("Step 7:Plot graph of K vs Accuracy")
    print(Border) 

    plt.figure(figsize=(8,5))
    plt.plot(K_values,accuracy_scores,marker='o')
    plt.title("K values vs Accuracy")
    plt.xlabel("Values of K")
    plt.ylabel("Accuracy")
    plt.grid(True)
    plt.xticks(list(K_values))
    plt.show()


    #Step 8:Find the best value of K
    print(Border)
    print("Step 8:Find the best value of K")
    print(Border) 
    best_k=list(K_values)[accuracy_scores.index(max(accuracy_scores))]
    print("Best Value of K:",best_k)

    
    #Step 9: Build final Model Using bet way of k
    print(Border)
    print("Step 9:Build final Model Using bet way of k")
    print(Border) 
    final_model=KNeighborsClassifier(n_neighbors=best_k)
    final_model.fit(X_train_scaled,Y_train)
    Y_pred=final_model.predict(X_test_scaled)


    #Step 10: Calculate Final Accuracy
    print(Border)
    print("Step 10: Calculate Final Accuracy")
    print(Border)

    accuracy=accuracy_score(Y_test,Y_pred)
    print("Accuracy of model is:",accuracy)

    #Step 11: Display Confusion Matrix
    print(Border)
    print("Step 11:Display Confusion matrix")
    print(Border) 

    cm=confusion_matrix(Y_test,Y_pred)
    print(cm)


    #Step 12: Display Classification report
    print(Border)
    print("Step 12:Display Classification report")
    print(Border) 

    print(classification_report(Y_test,Y_pred))

    print(Border) 


    
def main():
    Border="-"*40
    print(Border)

    print("Wine Classifier Using KNN")

    print(Border)

    MarvellousClassifier("WinePredictor.csv")


if __name__=="__main__":
    main()