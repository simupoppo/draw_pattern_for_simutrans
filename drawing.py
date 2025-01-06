import numpy as np
from PIL import Image
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import pandas as pd
import os
import sys




def draw_pattern(input_file, output_file, incolors,outcolors,divofouts,randommodes="linear",patternmodes=1):
    if os.path.isfile(input_file)==False:
        return 0
    else:
        imge = Image.open(input_file)
        #print(imge.mode)
        im = np.array(imge)
        #print(im.shape)
        imX = im.shape[0]
        imY = im.shape[1]
        if imge.mode == "RGBA":
            #f=open("img.txt","w")
            #for i in range(self.before):
            #    f.write("[")
            #    for j in range(self.before):
            #        f.write(str(im[i,j])+",")
            #    f.write("]\n")
            #f.close()
            #return 2
            modemode=2
        elif imge.mode=="RGB":
            modemode=0
        else:
            return 2
        #if imge.mode=="P":
        #    modemode=1
        #print(im[0,0])
        imgarray=drawing_tiles_program(im,incolors,outcolors,divofouts,modemode,randommodes,patternmodes)
        print("goodbye")
        output=Image.fromarray(imgarray)
        output.save(output_file)
        return 1
def drawing_tiles_program(inimg,incl,oucl,divcl,mode,randommode,patmode):
    print("loading")
    def tdrandm(input,pattern,centers,divss):
        # print(pattern,centers)
        if list(input) == pattern:
            #print("get",input,pattern)
            if patmode==3:
                temp_return=[int(randm(centers[0],divss[0],randommode))%256,int(randm(centers[1],divss[1],randommode))%256,int(randm(centers[2],divss[2],randommode))%256]
            else:
                if randommode == "gaussian":
                    temp_random=np.random.normal(loc=0,scale=1)
                else:
                    temp_random=np.random.rand(1)
                temp_return=[int(max(min(centers[0]-divss[0]+2*divss[0]*temp_random,255.1),0)),int(max(min(centers[1]-divss[1]+2*divss[1]*temp_random,255.1),0)),int(max(min(centers[2]-divss[2]+2*divss[2]*temp_random,255.1),0))]
            #print("yes")
            if mode==2:
                temp_return=resize_RGB(temp_return)
            for i in range(len(special_color_list)):
                if temp_return==special_color_list[i]:
                    temp_return[0]=temp_return[0]-int((temp_return[0]-128)/np.abs(temp_return[0]-128))
            #print(temp_return)
            return np.array(temp_return)
        else:
            return np.array(input)
    def randm(center,div,randommode):
        if randommode=="gaussian":
            return max(min(np.random.normal(loc=center,scale=div),255.1),0)       #Gaussian
        else:
            return max(min(center-div+2*div*np.random.rand(1),255.1),0)   #linear
    def resize_RGB(input):
        input=list(input)
        input.append(255)
        return input
    def resizing(inputsss):
        for i in range(len(inputsss)):
            #print(inputs,inputs[i])
            if len(inputsss[i])<4:
                inputsss[i]=resize_RGB(inputsss[i])
        return inputsss
    special_color_list=[[107,107,107],[155,155,155],[179,179,179],[201,201,201],[223,223,223],[127,155,241],[255,255,83],[255,33,29],[1,221,1],[227,227,255],[193,177,209],[77,77,77],[255,1,127],[1,1,255],[36,75,103],[57,94,124],[76,113,145],[96,132,167],[116,151,189],[136,171,211],[156,190,233],[176,210,255],[123,88,3],[142,111,4],[161,134,5],[180,157,7],[198,180,8],[217,203,10],[236,226,11],[255,249,13]]
    if mode==2:
        incl==resizing(incl)
        oucl==resizing(oucl)
        divcl==resizing(divcl)
        special_color_list=resizing(special_color_list)
    outimg=inimg
    for i in range(len(inimg)):
        for j in range(len(inimg[i])):
            if list(inimg[i][j])==[231,255,255]:
                outimg[i][j]=[231,255,255]
            elif list(inimg[i][j])==[231,255,255,255]:
                outimg[i][j]=[231,255,255,255]
            else:
                for kk in range(len(incl)):
                    outimg[i][j]=tdrandm(inimg[i][j],incl[kk],oucl[kk],divcl[kk])
                    #print(outimg[i][j],inimg[i][j])
                    if list(outimg[i][j])==list(inimg[i][j]):
                        jj=3
                        #print("yeah")
                    #elif list(outimg[i][j])==list(inimg[i][j]):
                        #print(kk)
                    else:
                        print("ohhh")
                        break
    outimg=np.array(outimg)
    outimg=outimg.astype(np.uint8)
    #print(outimg)
    #print(incl,oucl,divcl)
    print(outimg.shape,"done!")
    return outimg




def make_window():
    def ask_files():
        path=filedialog.askopenfilename()
        file_path.set(path)
        return
    def add_colorlist_from_csv():
        def errormessageofcsv():
            messagebox.showinfo("エラー","無効な書式です。色はRGBを各1要素ずつ合計9要素指定してください。")
            return
        pathofcsv=filedialog.askopenfilename()
        try:
            fileofcsv=pd.read_csv(pathofcsv,header=None,names=["incolorsR","incolorsG","incolorsB","outcolorsR","outcolorsG","outcolorsB","outcolordivsR","outcolordivsG","outcolordivsB"])
            for i in range(len(fileofcsv["incolorsR"])):
                if is_int(fileofcsv["incolorsR"][i])==True and is_int(fileofcsv["incolorsG"][i])==True and is_int(fileofcsv["incolorsB"][i])==True and is_int(fileofcsv["outcolorsR"][i])==True and is_int(fileofcsv["outcolorsG"][i])==True and is_int(fileofcsv["outcolorsB"][i])==True and is_int(fileofcsv["outcolordivsR"][i])==True and is_int(fileofcsv["outcolordivsG"][i])==True and is_int(fileofcsv["outcolordivsB"][i])==True:
                    incolor.append([fileofcsv["incolorsR"][i],fileofcsv["incolorsG"][i],fileofcsv["incolorsB"][i]])
                    outcolor.append([fileofcsv["outcolorsR"][i],fileofcsv["outcolorsG"][i],fileofcsv["outcolorsB"][i]])
                    outcolordiv.append([fileofcsv["outcolordivsR"][i],fileofcsv["outcolordivsG"][i],fileofcsv["outcolordivsB"][i]])
            input_color_list['text']=str(incolor)
            output_color_list["text"]=str(outcolor)
            return
        except:
            errormessageofcsv()
            return
    def reset_colors():
        incolor.clear()
        outcolor.clear()
        outcolordiv.clear()    
        input_color_list['text']=str(incolor)
        output_color_list["text"]=str(outcolor)
        return
    def howrandom():
        howhow=how_comb.get()
        if howhow=="正規分布":
            return "gaussian"
        elif howhow=="一様分布":
            return "linear"
    def howrondomdim():
        howdim=howdim_comb.get()
        if howdim=="3次元":
            return 3
        else:
            return 1
    def set_colors():
        incolor_temp_R=input_color_box_R.get()
        outcolor_temp_R=output_color_box_R.get()
        outcolor_div_temp_R=output_color_div_box_R.get()
        incolor_temp_G=input_color_box_G.get()
        outcolor_temp_G=output_color_box_G.get()
        outcolor_div_temp_G=output_color_div_box_G.get()
        incolor_temp_B=input_color_box_B.get()
        outcolor_temp_B=output_color_box_B.get()
        outcolor_div_temp_B=output_color_div_box_B.get()
        input_color_box_R.delete(0, tk.END)
        input_color_box_G.delete(0, tk.END)
        input_color_box_B.delete(0, tk.END)
        output_color_box_R.delete(0, tk.END)
        output_color_box_G.delete(0, tk.END)
        output_color_box_B.delete(0, tk.END)
        output_color_div_box_R.delete(0, tk.END)
        output_color_div_box_G.delete(0, tk.END)
        output_color_div_box_B.delete(0, tk.END)
        if is_int(incolor_temp_R)==True and is_int(incolor_temp_G)==True and is_int(incolor_temp_B)==True and is_int(outcolor_temp_R)==True and is_int(outcolor_temp_G)==True and is_int(outcolor_div_temp_B)==True and is_int(outcolor_div_temp_R)==True and is_int(outcolor_div_temp_G)==True and is_int(outcolor_div_temp_B)==True:
            incolor.append([int(incolor_temp_R),int(incolor_temp_G),int(incolor_temp_B)])
            outcolor.append([int(outcolor_temp_R),int(outcolor_temp_G),int(outcolor_temp_B)])
            outcolordiv.append([int(outcolor_div_temp_R),int(outcolor_div_temp_G),int(outcolor_div_temp_B)])
            #print(incolor)
            input_color_list['text']=str(incolor)
            output_color_list["text"]=str(outcolor)
            return
        messagebox.showinfo("エラー","RGB3色のlistを入力してください")
        return
    def app():
        input_file = file_path.get()
        output_file = filedialog.asksaveasfilename(
            filetype=[("PNG Image Files","*.png")],defaultextension=".png"
        )
        hows=howrandom()
        howdims=howrondomdim()
        print(output_file)
        if not input_file or not output_file or len(incolor)==0:
            return
        afterfile = draw_pattern(input_file,output_file,incolor,outcolor,outcolordiv,hows,howdims)
        if afterfile ==0:
            messagebox.showinfo("エラー","画像がありません")
        elif afterfile ==1:
            messagebox.showinfo("完了","完了しました。")
        elif afterfile ==2:
            messagebox.showinfo("エラー","画像サイズが正しくありません")
        return
    main_win = tk.Tk()
    main_win.title("draw_pattern_for_simutrans")
    main_win.geometry("700x300")
    main_frm = ttk.Frame(main_win)
    main_frm.grid(column=0, row=0, sticky=tk.NSEW, padx=5, pady=20)
    file_path=tk.StringVar()
    folder_label = ttk.Label(main_frm, text="ファイルを選択")
    csv_btn = ttk.Button(main_frm, text="CSVファイルから変換する色を選択",command=add_colorlist_from_csv)
    folder_box = ttk.Entry(main_frm,textvariable=file_path)
    folder_btn = ttk.Button(main_frm, text="選択",command=ask_files)
    input_color_label = ttk.Label(main_frm, text="置換前の色(RGB)")
    input_color_box_R = ttk.Entry(main_frm)
    input_color_box_G = ttk.Entry(main_frm)
    input_color_box_B = ttk.Entry(main_frm)
    input_color_list = ttk.Label(main_frm, text=str(incolor))
    output_color_label = ttk.Label(main_frm, text="置換後の色(RGB)")
    output_color_box_R = ttk.Entry(main_frm)
    output_color_box_G = ttk.Entry(main_frm)
    output_color_box_B = ttk.Entry(main_frm)
    output_color_list = ttk.Label(main_frm, text=str(outcolor))
    arrow_list=ttk.Label(main_frm,text="↓")
    output_color_div_label = ttk.Label(main_frm, text="色のゆらぎ(RGB)")
    how_label = ttk.Label(main_frm, text="色のゆらぎ方")
    how_comb = ttk.Combobox(main_frm, values=["正規分布","一様分布"], width=15)
    howdim_comb = ttk.Combobox(main_frm, values=["3次元","1次元"], width=15)
    how_comb.current(0)
    howdim_comb.current(0)
    output_color_div_box_R = ttk.Entry(main_frm)
    output_color_div_box_G = ttk.Entry(main_frm)
    output_color_div_box_B = ttk.Entry(main_frm)
    set_color_btn = ttk.Button(main_frm, text="設定")
    app_btn=ttk.Button(main_frm, text="変換を実行",command=app)
    addcolor_btn=ttk.Button(main_frm, text="色を追加", command=set_colors)
    resetcolor_btn=ttk.Button(main_frm, text="色の指定をリセット", command=reset_colors)
    folder_label.grid(column=0,row=0,pady=10)
    folder_box.grid(column=1,columnspan=2,row=0,sticky=tk.EW, padx=10)
    folder_btn.grid(column=3,row=0)
    input_color_box_R.grid(column=1,row=1,sticky=tk.EW, padx=5)
    input_color_box_G.grid(column=2,row=1,sticky=tk.EW, padx=5)
    input_color_box_B.grid(column=3,row=1,sticky=tk.EW, padx=5)
    input_color_label.grid(column=0,row=1)
    input_color_list.grid(column=1,columnspan=3,row=5)
    arrow_list.grid(column=2,row=6)
    output_color_list.grid(column=1,columnspan=3,row=7)
    output_color_box_R.grid(column=1,row=2,sticky=tk.EW, padx=5)
    output_color_box_G.grid(column=2,row=2,sticky=tk.EW, padx=5)
    output_color_box_B.grid(column=3,row=2,sticky=tk.EW, padx=5)
    output_color_label.grid(column=0,row=2)
    output_color_div_box_R.grid(column=1,row=3,sticky=tk.EW, padx=5)
    output_color_div_box_G.grid(column=2,row=3,sticky=tk.EW, padx=5)
    output_color_div_box_B.grid(column=3,row=3,sticky=tk.EW, padx=5)
    output_color_div_label.grid(column=0,row=3)
    how_label.grid(column=0,row=8)
    how_comb.grid(column=1,row=8,sticky=tk.W,padx=5)
    howdim_comb.grid(column=2,row=8,sticky=tk.W,padx=5)
    addcolor_btn.grid(column=1,columnspan=2,row=4)
    app_btn.grid(column=1,columnspan=2,row=9)
    resetcolor_btn.grid(column=3,row=9)
    csv_btn.grid(column=0,row=9)
    #main_win.columnconfigure(0, wieght=1)
    #main_win.rowconfigure(0, wieght=1)
    #main_frm.columnconfigure(1, wieght=1)
    main_win.mainloop()
    return
 
def is_int(s):
    try:
        int(s)
        if 0<=int(s)<=255:
            return True
        else:
            return False
    except ValueError:
        return False   
def helptext():
    print("このプログラムは、シムトランスのアドオン開発向けに画像の単色部分を塗り替えるプログラムです。")
    print("----------引数について---------------")
    print("引数無し GUIを起動します")
    print("-h ヘルプを表示します")
    print("(input file (csv)) (color file (csv)) [gaussian/linear] [3d/1d]  自動でファイルを作成します")
    print("input fileは出入力する画像名を指定します。csvファイルは必ず2列で、1列目に変換前の画像ファイル名を、2列目に変換後の画像ファイル名を入力してください。各行ごとに変換を行います。")
    print("color fileは変換する色の組み合わせをRGBで入力します。必ず9列で入力してください。")
    print("変換方法gaussian/linearはどちらかを入力してください。それ以外の入力の場合はgaussianモードで変換します。")
    print("色のばらつき方3d/1dは3dまたは1dを入力してください。それ以外の入力の場合1dモード(1次元的な色のばらつき)になります。")
    print("入力に不正がある場合、GUIが起動します。")
    return 
incolor=[]
outcolor=[]
outcolordiv=[]
if 3<=len(sys.argv)<=5:
    imagename=sys.argv[1]
    colorname=sys.argv[2]
    if os.path.isfile(imagename)==False:
        print("ファイルがありません")
        make_window()
    else:
        #print("ファイルはあります")
        try:
            #print("ok"+colorname+str(type(colorname))+str(os.path.isfile(colorname)))
            fileofcsv=pd.read_csv(colorname,header=None,names=["incolorsR","incolorsG","incolorsB","outcolorsR","outcolorsG","outcolorsB","outcolordivsR","outcolordivsG","outcolordivsB"])
            #print("ok"+str(type(fileofcsv["incolorsR"][0])))
            for i in range(len(fileofcsv["incolorsR"])):
                #print(str(is_int(1)))
                #print(str(i)+str(is_int(fileofcsv["incolorsR"][i]))+str(is_int(fileofcsv["incolorsG"][i]))+str(is_int(fileofcsv["incolorsB"][i]))+str(is_int(fileofcsv["outcolorsR"][i]))+str(is_int(fileofcsv["outcolorsG"][i]))+str(is_int(fileofcsv["outcolorsB"][i]))+str(is_int(fileofcsv["outcolordivsR"][i]))+str(is_int(fileofcsv["outcolordivsG"][i]))+str(is_int(fileofcsv["outcolordivsB"][i])))
                if is_int(fileofcsv["incolorsR"][i])==True and is_int(fileofcsv["incolorsG"][i])==True and is_int(fileofcsv["incolorsB"][i])==True and is_int(fileofcsv["outcolorsR"][i])==True and is_int(fileofcsv["outcolorsG"][i])==True and is_int(fileofcsv["outcolorsB"][i])==True and is_int(fileofcsv["outcolordivsR"][i])==True and is_int(fileofcsv["outcolordivsG"][i])==True and is_int(fileofcsv["outcolordivsB"][i])==True:
                    incolor.append([fileofcsv["incolorsR"][i],fileofcsv["incolorsG"][i],fileofcsv["incolorsB"][i]])
                    outcolor.append([fileofcsv["outcolorsR"][i],fileofcsv["outcolorsG"][i],fileofcsv["outcolorsB"][i]])
                    outcolordiv.append([fileofcsv["outcolordivsR"][i],fileofcsv["outcolordivsG"][i],fileofcsv["outcolordivsB"][i]])
            print("colorset done")
            try:
                fileofimages=pd.read_csv(imagename,header=None,names=["inputimg","outputimg"])
                for i in range(len(fileofimages["inputimg"])):
                    if os.path.isfile(str(fileofimages["inputimg"][i]))==False:
                        print(str(fileofimages["inputimg"][i])+"の画像がありません")
                    else:
                        if len(sys.argv)>3:
                            if sys.argv[3]=="linear":
                                hows="linear"
                            else:
                                hows="gaussian"
                            if len(sys.argv)==5:
                                if sys.argv[4]=="3d":
                                    dim=3
                                else:
                                    dim=1
                            else:
                                    dim=1
                        else:
                            hows="gaussian"
                            dim=1
                        draw_pattern(fileofimages["inputimg"][i],fileofimages["outputimg"][i],incolor,outcolor,outcolordiv,hows,dim)
            except:
                print("画像指定が不正です")
                make_window()
        except:
            print("色指定が不正です")
            make_window()
elif len(sys.argv)==2:
    if sys.argv[1]=="-help" or "-h":
        helptext()
    else:
        make_window()
else:
    make_window()