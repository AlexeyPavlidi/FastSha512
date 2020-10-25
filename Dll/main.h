#ifndef __MAIN_H__
#define __MAIN_H__

//#include <windows.h>
#include <stdint.h>

/*  To use this exported function of dll, include this header
 *  in your project.
 */

#ifdef BUILD_DLL
    #define DLL_EXPORT __declspec(dllexport)
#else
    #define DLL_EXPORT __declspec(dllimport)
#endif
//#define DATA_SZ 256
extern uint64_t  state[8];
extern uint64_t  length;
extern uint64_t  h0,h1,h2,h3,h4,h5,h6,h7;
//extern uint8_t   data[DATA_SZ];
//extern uint8_t  * data;
#endif // __MAIN_H__
