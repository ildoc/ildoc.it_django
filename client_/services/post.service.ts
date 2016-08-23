import {Http} from 'angular2/http';
import 'rxjs/add/operator/map';
import {Injectable} from 'angular2/core';

@Injectable()
export class PostService{
    private _url = "http://localhost:8000/apiv1/blog/";

    constructor(private _http: Http){

    }

    getPosts(){
        return this._http.get(this._url)
            .map(res => res.json());
    }

    createPost(post){
        return this._http.post(this._url, JSON.stringify(post))
            .map(res => res.json());
    }
}
