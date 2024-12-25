#include "ggml-cpp.h"
#include "ggml.h"
#include <llama.h>
#include <iostream>
#include <string>
#include <memory>

int main(){
    std::string model_path = "./Hello World";
    auto params = llama_context_default_params();
    std::cout<<model_path<<std::endl;
    // auto ctx = llama_(model_path.c_str(), params); 
    return 0;
}