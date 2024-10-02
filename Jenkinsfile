node {
  stage('SCM') {
    checkout scm
  }
  stage('SonarQube Analysis') {
    def scannerHome = tool 'SonarScanner';
    withSonarQubeEnv() {
      sh "${scannerHome}/bin/sonar-scanner"
    }
  }
  stage('pytest Execution') {
    sh 'python3 -m pytest ./tests/temp_coverage --junitxml="./pytest_result.xml" --html="./sample_testresult.html" --self-contained-html --cov-report xml --cov-branch --cov=src tests/temp_coverage/'
  }
}